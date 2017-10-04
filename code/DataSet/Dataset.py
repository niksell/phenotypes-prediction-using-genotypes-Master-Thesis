import numpy as np
from DataStructure.PatientPhenotype import PatientPhenotype
class DataSet:
    
    def __init__(self,patients,ids):
        
        self.__n = len(ids['patients']['nameToId'].keys())
        self.__m =len(ids['snps']['nameToId'].keys()) 
        self.__patients = patients
        self.__ids = ids
                     
        self.__xTable = np.zeros((self.__n,self.__m),dtype = int)
        self.__yTable = np.zeros((self.__n,),dtype = int)
        
        for i in range(self.__n):
            for j in range(self.__m):
                self.__xTable[i,j] = -1
   
                     
                     
    def __fillXTable(self):
    
        for i in range(self.__n):
            for j in range(self.__m):
        
                patient = self.__ids['patients']['idToName'][i]
                snp = self.__ids['snps']['idToName'][j]
        
                self.__xTable[i,j] = self.__patients[patient].getSnpCode(snp)
                     
    def __fillYTable(self):
    
        for i in range(self.__n):
    
            patient = self.__ids['patients']['idToName'][i]
            self.__yTable[i] = self.__patients[patient].getCase()
            
            
    def fillXTable1(self,patient,snp,code):
    
        
        i = self.__ids['patients']['nameToId'][patient]
        j = self.__ids['snps']['nameToId'][snp]
        self.__xTable[i,j] = code
                     
    def fillYTable1(self,patient):
    
        
        i = self.__ids['patients']['nameToId'][patient]
        self.__yTable[i] = self.__patients[patient].getCase()
        
    def getXTable(self):
                     
        return self.__xTable
                     
    def getYTable(self):
                     
        return self.__yTable