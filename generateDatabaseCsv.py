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
from rmgpy.kinetics import Arrhenius, Chebyshev, ThirdBody,Troe, KineticsData
import matplotlib.pyplot as plt

def getDatabaseType(directory):
    """
    This function takes a directory name and returns a string giving the type of database entry.
    """
    if os.path.isdir(directory):
        if os.path.exists(os.path.join(directory, 'rules.py')):
            return 'rules'
        #This includes depositories and libraries
        if re.search(re.escape('kinetics\libraries'), directory):
            return 'kineticsLibrary'
        if re.search('families.*training', directory):
            return 'trainingSet'
        
        
if __name__ == '__main__':
    # load database
    parser = argparse.ArgumentParser()
    parser.add_argument('file', metavar='FILE', type=str, nargs='?',
        help='the directory for the library or rules to export', default='all')
    parser.add_argument('output', metavar='OUTPUT', type=str, nargs='?', help='the csv where we give the ouput')
    parser.add_argument("-c", "--compare", action="store_true", help='use to make comparison with other data in the database')
    
    args = parser.parse_args()
    
    path = settings['database.directory']
    database = RMGDatabase()
    
    if args.file!='all':
        databaseType=getDatabaseType(args.file)
    #do entire database
    else: pass
        
    if databaseType=='kineticsLibrary':
        
        database.load(path,
             thermoLibraries=None,
             transportLibraries=None,
             reactionLibraries=[args.file],
             seedMechanisms=None,
             kineticsFamilies='none',
             kineticsDepositories=[],
             statmechLibraries=None,
             depository=True,
             solvation=True,
             )
        with open(args.output, 'wb') as csvfile:
            csvwriter=csv.writer(csvfile)
            entries=database.kinetics.libraries.values()[0].entries
            
            headingWritten=False
            for index in entries:
                kinetics=entries[index].data
                if type(kinetics) is Arrhenius:
                    if not headingWritten:
                        headingWritten=True
                        csvwriter.writerow(['Label', 'index', 'A (mol-sec-m^3)', 'n', 'Ea (kJ/mol)', 'T0 (K)', 'degeneracy'])           
                    csvwriter.writerow([entries[index].label, 
                                        index, 
                                        kinetics._A.value_si,
                                        kinetics._n.value_si, 
                                        kinetics._Ea.value_si,
                                        kinetics._T0.value_si,
                                        entries[index].item.degeneracy])
    
            #Need another for loop here
            #headingWritten=False
    if databaseType=='trainingSet':
        familyName=re.sub('.*families', '', args.file)
        familyName=re.sub('training', '', familyName)
        familyName=re.sub(re.escape('/'), '', familyName)
        familyName=re.sub('\\\\', '', familyName)
        database.load(path,
             thermoLibraries=None,
             transportLibraries=None,
             reactionLibraries=[],
             seedMechanisms=None,
             kineticsFamilies=[familyName],
             kineticsDepositories=[],
             statmechLibraries=None,
             depository=True,
             solvation=True,
             )
        
        templateDict={}
        duplicatesDict={}
        with open(args.output, 'wb') as csvfile:
            csvwriter=csv.writer(csvfile)
            entries=database.kinetics.families[familyName].depositories[0].entries
            
            headingWritten=False
            for index in entries:
                kinetics=entries[index].data
                template=database.kinetics.families[familyName].getReactionTemplate(entries[index].item)
                templateStr=''
                for group in template:
                    if templateStr!='': templateStr+=';'
                    templateStr+=group.label
                
                
                for key, value in templateDict.iteritems():
                    if templateStr==value[0]:
                        print entries[index].label, 'has matching template to', key, ' and may have other matches'
                        if not templateStr in duplicatesDict: duplicatesDict[templateStr]=[key]
                        duplicatesDict[templateStr].append(entries[index].label)
                        break
                templateDict[entries[index].label]=(templateStr,index)
                
                
                if type(kinetics) is Arrhenius:
                    if not headingWritten:
                        headingWritten=True
                        csvwriter.writerow(['Label', 'index', 'template', 'A (mol-sec-m^3)', 'n', 'Ea (J/mol)', 'T0 (K)', 'degeneracy', 'rank'])
                    try:
                        csvwriter.writerow([entries[index].label, 
                                            index, 
                                            templateStr,
                                            kinetics._A.value_si,
                                            kinetics._n.value_si, 
                                            kinetics._Ea.value_si,
                                            kinetics._T0.value_si,
                                            entries[index].item.degeneracy,
                                            entries[index].rank])
                    except ValueError: 
                        print entries[index].label + ' is missing some attribute'
                
        if args.compare:
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
                    
                
                          
    