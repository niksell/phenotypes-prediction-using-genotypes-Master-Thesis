import numpy as np

class PCA:
    
    def __init__(self,X,error = 0.9):
        
    
        self.matrix = X
        self.n = len(X)
        self.m = len(X.T)
        self.eigenValues = None
        self.eigenVectors = None
        self.F = None
        self.finalData = None
        self.selectedSnps = []
        self.eigenValuesPos = {}
        self.kEigenVectors = 0
        self.error = error
        self.meanMatrix = np.zeros((self.m,1),dtype = float)
        self.normalizedMatrix = np.zeros((self.n,self.m),dtype = float)
        self.covMatrix = None
        
        self.__calculateMeanMatrix()
        self.__normalizeMatrix()
        self.__calculateCovMatrix()
        self.__calculateEigenValuesAndEigenVectors()
        self.__findKEigenVectors()
        self.__createFMatrix()
        self.__createFinalMatrix()
                                  
    def __calculateMeanMatrix(self):
        
        for i in range(self.m):
            summ = 0
            for j in range(self.n):
                summ = self.matrix[j,i] + summ
                
            self.meanMatrix[i] = summ / self.n
            
    def __normalizeMatrix(self):
        
        for i in range(self.m):
            
            for j in range(self.n):
                
                self.normalizedMatrix[j,i] = self.matrix[j,i] - self.meanMatrix[i] 
            
    def __calculateCovMatrix(self):
       
        self.covMatrix = (self.normalizedMatrix.T.dot(self.normalizedMatrix)) / (self.n-1)
        print("cov = ",self.covMatrix.shape)

    def __calculateEigenValuesAndEigenVectors(self):
        
        eigen = np.linalg.eigh(self.covMatrix)
        self.eigenValues = eigen[0]
        self.eigenVectors = eigen[1]
            
        for i in self.eigenValues:
            self.eigenValuesPos[i] = []
            
        for i in range(len(self.eigenValues)):
            self.eigenValuesPos[self.eigenValues[i]].append(i)
            
        print("values = ",self.eigenValues)
        print("pos1 = ",self.eigenValuesPos[self.eigenValues[0]])
            
        self.eigenValues = sorted(self.eigenValues,reverse = True)
        print("values after = ",self.eigenValues)
        print("pos2 = ",self.eigenValuesPos[self.eigenValues[0]])
            
    def __findKEigenVectors(self):
        
        
        sumOfEigenValues = sum(self.eigenValues)
        summ = 0
        count = 0
        
        while (summ / sumOfEigenValues) - self.error < 1e-10:
            
            summ = summ + self.eigenValues[count]
            count += 1
            
        print("count is ",count)
        print("sum of eigenValues = ",sumOfEigenValues)
        print("sum is ",summ)
        
        self.kEigenVectors = count
        
    def __createFMatrix(self):
        
        self.F = np.zeros((self.m,self.kEigenVectors),dtype = float)
        
        for i in range(self.kEigenVectors):
            
            pos = self.eigenValuesPos[self.eigenValues[i]][0]
            self.selectedSnps.append(pos)
            self.eigenValuesPos[self.eigenValues[i]].remove(pos)
            
            self.F[:,i] = self.eigenVectors[:,pos]
                
        
    def __createFinalMatrix(self):
        
        self.finalData = self.matrix.dot(self.F)
        
        
    def getSelectedSnps(self):
        
        return self.selectedSnps
            
    def getFinalData(self,matrix = None):
        
        if matrix == None:
            
            return self.finalData
        
        else:
            
            return matirx.dot(self.F)