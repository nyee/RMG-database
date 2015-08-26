'''
This script is used to export the RMG-database to a human readable csv file. 

To use: input as the first argument the path to a library or depository folder, and a second argument path to an output csv file:
eg: python generateDatabaseCsv ~/RMG-database/input/kinetics/families/H_Abstraction/training ~/RMG-database/test.csv
'''
import os.path
import re
import csv
import argparse
from rmgpy.data.rmg import RMGDatabase
from rmgpy import settings
from rmgpy.kinetics import Arrhenius, Chebyshev, ThirdBody, Troe, KineticsData
import matplotlib.pyplot as plt

#List of types of databases within RMG and the desired attributes to be listed in a csv
databaseTypes={}
databaseTypes['kineticsRules']=[]
databaseTypes['kineticsLibrary']=['label', 'index', '_A', '_n', '_Ea', '_T0', 'degeneracy']
databaseTypes['trainingSet']=['label', 'index', 'template', '_A', '_n', '_Ea', '_T0', 'degeneracy', 'rank']



#What to write in the header of a csv for each variable
attributeToHeader={}
attributeToHeader['label']='Label'
attributeToHeader['index']='Index'
attributeToHeader['_A']='A'
attributeToHeader['_n']='n'
attributeToHeader['_Ea']='Ea'
attributeToHeader['_T0']='T0'
attributeToHeader['degeneracy']='degeneracy'
attributeToHeader['template']='template'
attributeToHeader['rank']='rank'

def getDatabaseType(directory):
    """
    This function takes a directory name and returns a string giving the type of database entry.
    """
    if os.path.isdir(directory):
        if os.path.exists(os.path.join(directory, 'rules.py')):
            return 'kineticsRules'
        #This includes depositories and libraries
        if re.search(re.escape('kinetics\libraries'), directory):
            return 'kineticsLibrary'
        if re.search('families.*training', directory):
            return 'trainingSet'

#Loads only the necessary parts of the RMG database for the desired part
def loadPartialDatabase(databaseType, directory):
    database = RMGDatabase()
    name=''
    if databaseType=='kineticsLibrary':
        database.load(path,
             thermoLibraries=None,
             transportLibraries=None,
             reactionLibraries=[directory],
             seedMechanisms=None,
             kineticsFamilies='none',
             kineticsDepositories=[],
             statmechLibraries=None,
             depository=True,
             solvation=True,
             )
        entries=database.kinetics.libraries.values()[0].entries
    
    elif databaseType=='trainingSet':
        name=re.sub('.*families', '', args.file)
        name=re.sub('training', '', name)
        name=re.sub(re.escape('/'), '', name)
        name=re.sub('\\\\', '', name)
        database.load(path,
             thermoLibraries=None,
             transportLibraries=None,
             reactionLibraries=[],
             seedMechanisms=None,
             kineticsFamilies=[name],
             kineticsDepositories=[],
             statmechLibraries=None,
             depository=True,
             solvation=True,
             )
        entries=database.kinetics.families[name].depositories[0].entries

    return database, entries, name

#creates a line to be written in the csv
def getAttributes(entry, databaseType):
    line=[]
    commonAttributes=['index',
                      'label',
                      'item',
                      'parent',
                      'children',
                      'data',
                      'reference',
                      'referenceType',
                      'shortDesc',
                      'longDesc',
                      'rank']
    dataAttributes=['_A', 
                    '_n', 
                    '_Ea', 
                    '_T0',]
    itemAttributes=['degeneracy',]
    for attribute in databaseTypes[databaseType]:
        if attribute in commonAttributes: line.append(getattr(entry, attribute))
        elif attribute in dataAttributes: line.append(getattr(entry.data, attribute))
        elif attribute in itemAttributes: line.append(getattr(entry.item, attribute))
        elif attribute=='template': 
            template=database.kinetics.families[name].getReactionTemplate(entry.item)
            templateStr=''
            for group in template:
                if templateStr!='': templateStr+=';'
                templateStr+=group.label
            line.append(templateStr)
        else: raise AttributeError("Cannot find attribute")
    return line
if __name__ == '__main__':
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE', type=str, nargs='?',
        help='the directory for the library or rules to export', default='all')
    parser.add_argument('output', metavar='OUTPUT', type=str, nargs='?', help='the csv where we give the ouput')
    parser.add_argument("-c", "--compare", action="store_true", help='use to make comparison with other data in the database')
    args = parser.parse_args()
    
    path = settings['database.directory']
    
    if args.file!='all':
        databaseType=getDatabaseType(args.file)
        database, entries, name = loadPartialDatabase(databaseType, args.file)
        csvList=[]
        
        headingWritten=False
        for index in entries:
            kinetics=entries[index].data
            if type(kinetics) is Arrhenius:
                if not headingWritten: 
                    headingWritten=True
                    heading= [attributeToHeader[attribute] for attribute in databaseTypes[databaseType]]
                    csvList.append(heading)
                try:
                    csvList.append(getAttributes(entries[index], databaseType))
                except ValueError: 
                    print entries[index].label + ' is missing some attribute'
                    
                    
        with open(args.output, 'wb') as csvfile:
            csvwriter=csv.writer(csvfile)
            for line in csvList:
                csvwriter.writerow(line)
    #generateCsv for entire database
    else: pass
                  

            
                
    if args.compare:
        templateDict={}
        duplicatesDict={}
        
        for line in csvList:
            if type(line[1]) is int:
                label=line[0]
                index=line[1]
                templateStr=line[2]    
                for key, value in templateDict.iteritems():
                    if templateStr==value[0]:
                        print label, 'has matching template to', key, ' and may have other matches'
                        if not templateStr in duplicatesDict: duplicatesDict[templateStr]=[key]
                        duplicatesDict[templateStr].append(label)
                        break
                templateDict[label]=(templateStr,index)
        
        TList=range(300,2100,100)
        inverseTList=[1000.0/T for T in TList]
        for key, duplicates in duplicatesDict.iteritems():
            plt.figure()
            for reactionStr in duplicates:
                index=templateDict[reactionStr][1]
                kinetics=entries[index].data
                kList=[kinetics.getRateCoefficient(T)/entries[index].item.degeneracy for T in TList]
                plt.semilogy(inverseTList,kList,label=reactionStr)
            plt.title('Training reactions with template '+ key)
            plt.xlabel("1000 / Temperature (1000/K)")
            plt.ylabel("Rate coefficient")
            plt.legend()
            plt.show()
                               
                          
    