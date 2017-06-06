import numpy as np
from DataStructure.PatientPhenotype import PatientPhenotype
class DataSet:
    
    def __init__(self,patients,ids):
        
        self.n = len(ids['patients']['nameToId'].keys())
        self.m =len(ids['snps']['nameToId'].keys()) 
        self.patients = patients
        self.ids = ids
                     
        self.xTable = np.zeros((self.n,self.m),dtype = int)
        self.yTable = np.zeros((self.n,),dtype = int)
        
        for i in range(self.n):
            for j in range(self.m):
                self.xTable[i,j] = -1
                     
        self.__fillXTable()
        self.__fillYTable()
                     
                     
    def __fillXTable(self):
    
        for i in range(self.n):
            for j in range(self.m):
        
                patient = self.ids['patients']['idToName'][i]
                snp = self.ids['snps']['idToName'][j]
        
                self.xTable[i,j] = self.patients[patient].getSnpCode(snp)
                     
    def __fillYTable(self):
    
        for i in range(self.n):
    
            patient = self.ids['patients']['idToName'][i]
            self.yTable[i] = self.patients[patient].getCase()
        
    def getXTable(self):
                     
        return self.xTable
                     
    def getYTable(self):
                     
        return self.yTable