import numpy as np
import math

class Correlation():
    
    def __init__(self,X):
        
        self.n = len(X)
        self.m = len(X.T)
        self.matrix = X
        self.meanMatrix = np.zeros((self.m,1))
        self.covMatrix = None
        self.correlationMatrix = np.zeros((self.m,self.m),dtype = float)
        self.varMatrix = np.zeros((self.m),dtype = float)
        self.normalizedMatrix = np.zeros((self.n,self.m),dtype = float)
        
        self.__calculateMeanMatrix()
        self.__normalizeMatrix()
        self.__calculateCovMatrix()
        self.__calculateVar()
        self.__calclulateCorr()
        
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
       
        self.covMatrix = (self.normalizedMatrix.T.dot(self.normalizedMatrix)) / (self.n - 1)
        
        
    def __calculateVar(self):
        
        for i in range(self.m):
            
            self.varMatrix[i] = math.sqrt((self.normalizedMatrix[:,i].dot(self.normalizedMatrix[:,i])) / (self.n-1 )) 
    
    def __calclulateCorr(self):
        
        for i in range(self.m):
            
            for j in range(i,self.m):
                
                    
                result1 = self.covMatrix[i,j]
                result2 = self.varMatrix[i]
                result3 = self.varMatrix[j]
                result = result1 / (result2 * result3)
                
                self.correlationMatrix[i,j] = result
                self.correlationMatrix[j,i] = result
                
    def getCorrMatrix(self):
        
        return self.correlationMatrix