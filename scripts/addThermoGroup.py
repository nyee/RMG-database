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
        #Makes a list of each ancestors depth in the tree
        depthAncestorList=[database.getTreeDepth(x) for x in ancestorList]
        maxDepth=max(depthAncestorList)
        directParents=[]
        for index, depth in enumerate(depthAncestorList):
            if depth==maxDepth:
                directParents.append(ancestorList[index])
        ancestorList=directParents

    return ancestorList

def getDescendentsForNewNode(database, newNode, direct=False):
    """
    Returns a list of all nodes currently in database that are childen for newNode
    """
    descendantsList=[]
    for name, entry in database.entries.iteritems():
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

def identicalData(oldNode, newNode):
    """
    Returns true if two nodes have exactly the same numbers for ThermoData
    """

    if oldNode.data is None and newNode.data is None:
        return True

    if isinstance(oldNode.data, ThermoData) and isinstance(newNode.data, ThermoData):
        dataToCheck=["H298.value_si",
                     "H298.uncertainty_si",
                     "S298.value_si",
                     "S298.uncertainty_si",
                     "Tdata.value_si",
                     "Cpdata.value_si",
                     "Cpdata.uncertainty_si"]
        data1=[]
        data2=[]
        for data in dataToCheck:
            if isinstance(getattr(oldNode.data, data)) is float:
                data1.append(getattr(oldNode.data, data))
                data2.append(getattr(newNode.data, data))
            else:
                data1.extend(getattr(oldNode.data, data))
                data2.extend(getattr(newNode.data, data))

        for check1, check2 in zip(data1, data2):
            if not check1==check2:
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
        print '{:<40}'.format(heading1), '{:<40}'.format(heading2)
    for line1, line2, in zip(newlist1, newlist2):
        if len(str(line1))>37 or len(str(line2))>37:
            str1=str(line1)
            str2=str(line2)
            chunks1, chunks2, chunk_size = len(str1), len(str2), 37
            newList1=[str1[i:i+chunk_size] for i in range(0, chunks1, chunk_size)]
            newList2=[str2[i:i+chunk_size] for i in range(0, chunks2, chunk_size)]
            sideBySidePrint(newList1, newList2)
        else: print '{:<40}'.format(line1), '{:<40}'.format(line2)

def findPlaceInTree(database, newNode):
    """
    Prints information about location in tree for newNode
    """
    #Check for matching node:
    identical=identicalGroup(database, newNode)
    if identical: return (identical.parent, identical, identical.children)

    #check for overlapping parents
    directParents=getAncestorsForNewNode(database, newNode, True)

    if len(directParents)>1:
        sideBySidePrint(re.split(r'\n', directParents[0].item.toAdjacencyList()),
                        re.split(r'\n', directParents[1].item.toAdjacencyList()),
                        directParents[0].label, directParents[1].label)
        raise Exception("There is more than one direct parent for", newNode.label, "which are", str(directParents))
    else:
        parent=directParents[0]
        # print "There is one parent for", newNode.label, "which is", parent.label

    #Check direct children have "parent" as parent
    directChildren=getDescendentsForNewNode(database, newNode, True)
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
    """

    dataInfo=["data", "shortDesc", "reference", "rank"]

    #make a deep copy to scan through: Because of the isomorphism checks, we scramble the adjLists
    #so we scan through the copy, but actually edit the original
    print newNode.label
    # databaseCopy=copy.deepcopy(database)
    databaseCopy=database
    treeInfo=findPlaceInTree(databaseCopy, newNode)

    #define variables for the relatives in the original database
    (parentCopy, identicalCopy, directChildrenCopy)=treeInfo
    parent=database.entries[parentCopy.label]
    if identicalCopy:
        identical=database.entries[identicalCopy.label]
    directChildren=[database.entries[child.label] for child in directChildrenCopy]

    if not identicalCopy is None:
        #if identical has pointer for Thermo, copy data and all metaData
        if isinstance(identical.data, basestring):
            replaceData(identical, newNode)
        elif identical.label == newNode.label and identicalData(identical, newNode):
            print newNode.label, "already added!"
        else:

            print identical, "and", newNode, "are identical and both have ThermoObjects."
            sideBySidePrint([attr+": "+ str(getattr(identical, attr)) for attr in dataInfo],
                            [attr+": "+ str(getattr(newNode, attr)) for attr in dataInfo],
                            heading1=identical.label + "'s data",
                            heading2=newNode.label + "'s data")
            print "type 0 to keep old entry, 1 to replace with new entry"
            #write code for user to decide which one to use
            choice=raw_input()
            if choice=='0':
                print identical, "data was left"
            elif choice=='1':
                print identical, "data was replaced"
                replaceData(identical, newNode)
    else:
        #This is the case where the new node is completely new
        print "Adding", newNode
        database.entries[newNode.label]=newNode
        #check this where does it go, end?
        newNode.parent=parent
        parent.children.append(newNode)
        newNode.children=directChildren

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

if __name__ == "__main__":
    path="/Users/Nate/Dropbox (MIT)/Research/RMG/thermo/oxy_species2.py"
    newGroups = ThermoGroups()
    newGroups.local_context['ThermoData']=ThermoData
    newGroups.load(path)
    outputPath="/Users/Nate/Dropbox (MIT)/Research/RMG/thermo/parents.txt"
    groupName='group'

    database = RMGDatabase()
    database.load(settings['database.directory'], thermoLibraries = [], kineticsFamilies='all', kineticsDepositories=[], reactionLibraries=[])

    # specificGroupDatabase = database.thermo.groups[groupName]
    # savePath= os.path.join(settings['database.directory'], "thermo/groups/"+specificGroupDatabase.label+".py")
    #
    
    family= database.kinetics.families['H_Abstraction']
    specificGroupDatabase=family.groups
    savePath= os.path.join(settings['database.directory'], "kinetics/families/"+family.label)
    modified=fixParents(specificGroupDatabase)
    if modified:
        family.save(savePath)



    # for entryName, entry in newGroups.entries.iteritems():
    #     addThermoGroup(specificGroupDatabase, entry)
    #     specificGroupDatabase.save(savePath)


    # test1=specificGroupDatabase.entries["C"].data
    # # print test1
    # # testGroup=newGroups.entries['Cs-CsCsCsOs']
    # # print getAncestorsForNewNode(specificGroupDatabase, testGroup)
    # # print getDescendentsForNewNode(specificGroupDatabase, testGroup)
    # # print checkIdenticalNode(specificGroupDatabase, testGroup)
    #
    # for name, entry in newGroups.entries.iteritems():
    #     print name
    #     print findPlaceInTree(specificGroupDatabase, entry)