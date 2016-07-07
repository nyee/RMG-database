#!/usr/bin/env python
# encoding: utf-8

"""
This script adds entries from a file into the RMG-database.

Inputs?
"""
from rmgpy.data.thermo import *
from rmgpy.thermo import ThermoData
from rmgpy.data.rmg import RMGDatabase
from rmgpy import settings
import re
import copy
import os.path
from rmgpy.data.base import LogicOr
from rmgpy.molecule import Group
from numpy import round

dataToCheck=["H298.value_si",
             "H298.uncertainty_si",
             "S298.value_si",
             "S298.uncertainty_si",
             "Tdata.value_si",
             "Cpdata.value_si",
             "Cpdata.uncertainty_si"]

def getAncestorsForNewNode(database, newNode, direct=False):
    """
    Returns a list of all nodes currently in database that are parents for newNode
    If the argument direct is used, then only the ancestors with the highest tree depth will be returned
    """
    ancestorList=[]
    for name, entry in database.entries.iteritems():
        if database.matchNodeToChild(entry, newNode):
            ancestorList.append(entry)

    if direct:
        directParents = []
        #Makes a list of each ancestors depth in the tree
        while ancestorList:
            depthAncestorList=[database.getTreeDepth(x) for x in ancestorList]
            maxDepth=max(depthAncestorList)
            for index, depth in enumerate(depthAncestorList):
                if depth==maxDepth:
                    directParents.append(ancestorList[index])

            #test ancestorList only has one "branch"
            for parent in directParents:
                newAncestor = parent
                if newAncestor in ancestorList:
                    ancestorList.remove(newAncestor)
                while newAncestor.parent:
                    newAncestor = newAncestor.parent
                    if newAncestor in ancestorList:
                        ancestorList.remove(newAncestor)

        #If things left over, then we have more than one potential parent

        if len(directParents) > 1:
            print "More than one parent possible for", newNode.label, "Picking first found in pre-order "
            #write code for user to decide which one to use
            match = database.preOrderSearch(directParents, database.top[0])
            ancestorList=[match]
        else: ancestorList= directParents
    return ancestorList

def getDescendentsForNewNode(database, newNode, parent, direct=False):
    """
    Returns a list of all nodes currently in database that are childen for newNode

    parent is the parent of the newNode
    """
    descendantsList=[]
    for entry in parent.children:
        if database.matchNodeToChild(newNode, entry):
            descendantsList.append(entry)

    if direct:
        directChildList=[]
        for descendant in descendantsList:
            if not descendant.parent in descendantsList:
                directChildList.append(descendant)
        descendantsList=directChildList

    return descendantsList

def identicalGroup(database, newNode):
    """
    Returns the a node structurally identical to newNode if it exists in the database
    """
    for name, entry in database.entries.iteritems():
        if database.matchNodeToNode(entry, newNode):
            return entry
    else: return None

def getDataForComparison(oldNode, newNode):
    """
    returns oldData, newData, two tuples with values from the two nodes
    """

    oldData = {}
    newData = {}

    data1=[]
    data2=[]
    for property in dataToCheck:
        oldData[property] = []
        newData[property] = []
        if isinstance(reduce(getattr, property.split("."), oldNode.data), float):
            oldData[property].append(reduce(getattr, property.split("."), oldNode.data))
            newData[property].append(reduce(getattr, property.split("."), newNode.data))
        else:
            oldData[property].extend(reduce(getattr, property.split("."), oldNode.data))
            newData[property].extend(reduce(getattr, property.split("."), newNode.data))

    return (oldData, newData)

def identicalData(oldNode, newNode):
    """
    Returns true if two nodes have exactly the same numbers for ThermoData
    """

    if oldNode.data is None and newNode.data is None:
        return True

    if isinstance(oldNode.data, ThermoData) and isinstance(newNode.data, ThermoData):
        (oldData, newData) = getDataForComparison(oldNode, newNode)

        for property in oldData.keys():
            for index in range(len(oldData[property])):
                if not oldData[property][index]==newData[property][index]:
                    return False
        else: return True
        
    else: return False

def sideBySidePrint(list1, list2, heading1=None, heading2=None):
    """
    This function prints two lists side by side even if they are of different lengths
    """
    newlist1=[x for x in list1]
    newlist2=[x for x in list2]


    if len(list1) > len(list2):
        for x in range(len(list1)-len(list2)):
            newlist2.append('')
    elif len(list2) > len(list1):
        for x in range(len(list2)-len(list1)):
            newlist1.append('')

    if heading1:
        print '{:<80}'.format(heading1), '{:<80}'.format(heading2)
    for line1, line2, in zip(newlist1, newlist2):
        if len(str(line1))>77 or len(str(line2))>77:
            str1=str(line1)
            str2=str(line2)
            chunks1, chunks2, chunk_size = len(str1), len(str2), 77
            newList1=[str1[i:i+chunk_size] for i in range(0, chunks1, chunk_size)]
            newList2=[str2[i:i+chunk_size] for i in range(0, chunks2, chunk_size)]
            sideBySidePrint(newList1, newList2)
        else: print '{:<80}'.format(line1), '{:<80}'.format(line2)

def findPlaceInTree(database, newNode):
    """
    Prints information about location in tree for newNode
    """
    #Check for matching node:
    identical=identicalGroup(database, newNode)
    if identical: return (identical.parent, identical, identical.children)

    #check for overlapping parents
    directParents=getAncestorsForNewNode(database, newNode, True)
    parent = directParents[0]

    #Check direct children have "parent" as parent
    directChildren=getDescendentsForNewNode(database, newNode, parent, True)
    for child in directChildren:
        if not child.parent==parent:
            print "Child node", child.label, "(parent:", child.parent.label, ") is a child of the new node", \
                newNode.label, "but not the direct child of its parent", parent.label
            sideBySidePrint(re.split(r'\n', child.item.toAdjacencyList()),
                            re.split(r'\n', parent.item.toAdjacencyList()),
                            child.label, parent.label)
            sideBySidePrint(re.split(r'\n', child.parent.item.toAdjacencyList()),
                            re.split(r'\n', newNode.item.toAdjacencyList()),
                            child.parent.label, newNode.label)

    return (parent, identical, directChildren)

def replaceData(oldNode, newNode):
    """
    Replaces all data and metadata for an old entry with data from the new entry
    """
    oldNode.data=newNode.data
    oldNode.reference = newNode.reference
    oldNode._longDesc = newNode._longDesc
    oldNode._shortDesc = newNode._shortDesc
    oldNode._longDesc = newNode.longDesc
    oldNode._shortDesc = newNode.shortDesc
    oldNode.rank = newNode.rank
    oldNode.referenceType = newNode.referenceType

def addThermoGroup(database, newNode, rePoint=False):
    """
    Returns a new database object with newNode added correctly into the database

    treeInfo is the tuple returned from findPlaceInTree

    rePoint is whether we want the children of the newNode to point toward the newly added group (only if they
    were originally basestrings already)
    """

    dataInfo=["shortDesc", "reference", "rank"]

    print newNode.label

    if newNode.item.standardizeGroup():
        print newNode.label, "has been modified by standardizeGroup:"
        print re.split(r'\n', newNode.item.toAdjacencyList())
    #make a deep copy to scan through: Because of the isomorphism checks, we scramble the adjLists
    #so we scan through the copy, but actually edit the original
    # databaseCopy=copy.deepcopy(database)
    # databaseCopy=database
    treeInfo=findPlaceInTree(database, newNode)

    #define variables for the relatives in the original database
    (parentCopy, identicalCopy, directChildrenCopy)=treeInfo
    parent=database.entries[parentCopy.label]
    if identicalCopy:
        identical=database.entries[identicalCopy.label]
    directChildren=[database.entries[child.label] for child in directChildrenCopy]

    if identicalCopy:
        #if identical has pointer for Thermo, copy data and all metaData
        if isinstance(identical.data, basestring):
            replaceData(identical, newNode)
            print identical.label, "had pointer data replaced by data from", newNode.label
        elif identicalData(identical, newNode):
            print newNode.label, "already added!"
        else:
            print identical, "and", newNode, "are identical and both have ThermoObjects."
            (oldData, newData) = getDataForComparison(identical, newNode)

            sideBySidePrint([property + ': ' + str(round(oldData[property], 2)) for property in dataToCheck],
                [property + ': ' + str(round(newData[property],2)) for property in dataToCheck],
                heading1=identical.label + "'s data",
                heading2=newNode.label + "'s data")

            sideBySidePrint([attr+": "+ str(getattr(identical, attr)) for attr in dataInfo],
                            [attr+": "+ str(getattr(newNode, attr)) for attr in dataInfo])
            print "type 0 to keep old entry, 1 to replace with new entry"
            #write code for user to decide which one to use
            choice=raw_input()
            while (not choice == '1') and (not choice == '0'):
                print "type 0 to keep old entry, 1 to replace with new entry"
                choice = raw_input()
            if choice=='0':
                print identical, "data was left"
            elif choice=='1':
                print identical, "data was replaced"
                replaceData(identical, newNode)
    else:
        #This is the case where the new node is completely new
        print "Adding", newNode.label, "with parent", parent.label
        database.entries[newNode.label]=newNode
        #check this where does it go, end?
        sideBySidePrint(re.split(r'\n', newNode.item.toAdjacencyList()),
                re.split(r'\n', parent.item.toAdjacencyList()),
                newNode.label, parent.label)
        print "With children {0}".format([x.label for x in directChildren])
        print "With siblings {0}".format([x.label for x in parent.children])
        newNode.parent=parent
        parent.children.append(newNode)
        newNode.children=directChildren
        choice=raw_input()

        #remove children from parent
        for child in directChildren:
            parent.children.remove(child)
            child.parent=newNode

        if rePoint:
            #check data of children
            for child in directChildren:
                if isinstance(child.data, basestring):
                    targetName=child.data.strip()
                    target=database.entries[targetName]
                    if database.getTreeDepth(target) < database.getTreeDepth(newNode):
                        print "Changed thermo data for", child
                        child.data=unicode(newNode.label)

def fixParents(database):
    """
    This function removes groups that fail childParentCheck and siblingCheck and then
    adds them back into to the correct place
    """
    entriesRemoved={}
    for nodeName, childNode in database.entries.iteritems():
    #top nodes and product nodes don't have parents by definition, so they get an automatic pass:
        if childNode in database.top: continue
        parentNode = childNode.parent
        # Check whether the node has proper parents unless it is the top reactant or product node
        # The parent should be more general than the child
        if not database.matchNodeToChild(parentNode, childNode):
            entriesRemoved[nodeName]=childNode
            database.removeGroup(childNode)
            continue

        #check that parentNodes which are LogicOr do not have an ancestor that is a Group
        #If it does, then the childNode must also be a child of the ancestor
        if isinstance(parentNode, LogicOr):
            ancestorNode = childNode
            while ancestorNode not in database.top and isinstance(ancestorNode, LogicOr):
                ancestorNode = ancestorNode.parent
            if isinstance(ancestorNode, Group):
                if not database.matchNodeToChild(parentNode, childNode):
                    entriesRemoved[nodeName]=childNode
                    database.removeGroup(childNode)

    #Now check siblings
    for nodeName, node in database.entries.iteritems():
        for index, child1 in enumerate(node.children):
            for child2 in node.children[index+1:]:
                #Don't check a node against itself
                if child1 is child2: continue
                if database.matchNodeToChild(child1, child2):
                    #get nodename (not same as label for rules)
                    for key, value in database.entries.iteritems():
                        if value==child2:
                            entriesRemoved[key]=child2
                            database.removeGroup(child2)
                            break
                if database.matchNodeToChild(child2, child1):
                    #get nodename (not same as label for rules)
                    for key, value in database.entries.iteritems():
                        if value==child1:
                            entriesRemoved[key]=child1
                            database.removeGroup(child1)
                            break

    if not entriesRemoved: return False
    #Remove groups should have no parents or children to function properly
    print entriesRemoved.keys()
    for nodeName, node in entriesRemoved.iteritems():
        node.parent=None
        node.children=[]
    #Add groups
    for nodeName, node in entriesRemoved.iteritems():
        addThermoGroup(database, node)
    return True

def fixIdentical(database):
    """
    Removes identical nodes from a database
    """
    entriesCopy = copy.copy(database.entries)
    for nodeName, nodeGroup in database.entries.iteritems():
        del entriesCopy[nodeName]
        for nodeNameOther, nodeGroupOther in entriesCopy.iteritems():
            # try:
            if database.matchNodeToNode(nodeGroup,nodeGroupOther):
                print nodeName, "will be removed because it is the same as", nodeNameOther
                database.removeGroup(nodeGroup)
                break
            # except:
            #     print "something went wrong"
            #     print nodeName
            #     print nodeNameOther

if __name__ == "__main__":
    # path="/Users/Nate/Dropbox (MIT)/Research/RMG/thermo/oxygenates/oxy_species2.py"
    path="/Users/Nate/Dropbox (MIT)/Research/RMG/thermo/oxygenates/HBI_2.py"
    newGroups = ThermoGroups()
    newGroups.local_context['ThermoData']=ThermoData
    newGroups.load(path)
    outputPath="/Users/Nate/Dropbox (MIT)/Research/RMG/thermo/parents.txt"
    groupName='group'
    groupName = 'radical'

    database = RMGDatabase()
    database.load(settings['database.directory'], thermoLibraries = [], kineticsFamilies='all', kineticsDepositories=[], reactionLibraries=[])

    specificGroupDatabase = database.thermo.groups[groupName]
    savePath= os.path.join(settings['database.directory'], "thermo/groups/"+specificGroupDatabase.label+".py")
    for entryName, newNode in newGroups.entries.iteritems():
        addThermoGroup(specificGroupDatabase,newNode, True)
        specificGroupDatabase.save(savePath)

    
    # family= database.kinetics.families['Substitution_O']
    # specificGroupDatabase=family.groups
    # savePath= os.path.join(settings['database.directory'], "kinetics/families/"+family.label)
    # modified=fixParents(specificGroupDatabase)
    # if modified:
    #     family.save(savePath)
    # fixIdentical(specificGroupDatabase)
