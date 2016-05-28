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

def getAncestorsForNewNode(database, newNode):
    """
    Returns a list of all nodes labels currently in database that are parents for newNode
    """
    ancestorList=[]
    for name, entry in database.entries.iteritems():
        if database.matchNodeToChild(entry, newNode):
            ancestorList.append(name)

    return ancestorList

def getDescendentsForNewNode(database, newNode):
    """
    Returns a list of all nodes labels currently in database that are childen for newNode
    """
    DescendentsList=[]
    for name, entry in database.entries.iteritems():
        if database.matchNodeToChild(newNode, entry):
            DescendentsList.append(entry)

    return DescendentsList

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


    testGroup=newGroups.entries['Cs-CsCsCsOs']
    print getAncestorsForNewNode(specificThermoDatabase, testGroup)
    print getDescendentsForNewNode(specificThermoDatabase, testGroup)