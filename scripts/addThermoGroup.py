#!/usr/bin/env python
# encoding: utf-8

"""
This script adds entries from a file into the RMG-database.

Inputs?
"""
from rmgpy.data.thermo import *
from rmgpy.data.rmg import RMGDatabase
from rmgpy import settings
import re
import copy
import os.path
from rmgpy.thermo import *

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

def checkIdenticalNode(database, newNode):
    """
    Returns the a node structurally identical to newNode if it exists in the database
    """
    for name, entry in database.entries.iteritems():
        if database.matchNodeToNode(entry, newNode):
            return entry
    else: return None

def findPlaceInTree(database, newNode):
    """
    Prints information about location in tree for newNode
    """
    #Check for matching node:
    identical=checkIdenticalNode(database, newNode)
    if identical:
        print "There is already an identical node for", newNode.label, "which is", identical

    #check for overlapping parents
    directParents=getAncestorsForNewNode(database, newNode, True)

    if len(directParents)>1:
        print "There is more than one direct parent for", newNode.label, "which are", str(directParents)
        return (None, identical, [])
    else:
        parent=directParents[0]
        print "There is one parent for", newNode.label, "which is", parent.label

    #Check direct children have "parent" as parent
    directChildren=getDescendentsForNewNode(database, newNode, True)
    for child in directChildren:
        if not child.parent==parent:
            print "Child node", child.label, "is a child of the new node", newNode.label, \
                "but not a child of its parent", parent.label

    return (parent, identical, directChildren)


if __name__ == "__main__":
    path="/Users/Nate/Dropbox (MIT)/Research/RMG/thermo/oxy_species2.py"
    newGroups = ThermoGroups()
    newGroups.local_context['ThermoData']=ThermoData
    newGroups.load(path)
    outputPath="/Users/Nate/Dropbox (MIT)/Research/RMG/thermo/parents.txt"
    groupName='group'
    topGroupName="R"

    database = RMGDatabase()
    database.load(settings['database.directory'], thermoLibraries = [], kineticsFamilies='none', kineticsDepositories='none', reactionLibraries=[])

    specificThermoDatabase = database.thermo.groups[groupName]

    test1=specificThermoDatabase.entries["C"].data
    # print test1
    # testGroup=newGroups.entries['Cs-CsCsCsOs']
    # print getAncestorsForNewNode(specificThermoDatabase, testGroup)
    # print getDescendentsForNewNode(specificThermoDatabase, testGroup)
    # print checkIdenticalNode(specificThermoDatabase, testGroup)

    for name, entry in newGroups.entries.iteritems():
        print name
        print findPlaceInTree(specificThermoDatabase, entry)