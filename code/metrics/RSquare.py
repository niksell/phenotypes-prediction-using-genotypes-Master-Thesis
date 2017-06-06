import numpy as np
import math

class RSquare():
    
    def __init__(self,X):
        
        self.matrix = X
        self.n = len(X)
        self.m = len(X.T)
        self.sumColumn = np.zeros((self.m))
        self.sumColumnSquare = np.zeros((self.m))
        self.poll = None
        self.rMatrix = np.zeros((self.m,self.m))
        
        self.__sum()
        self.__sumSquare()
        self.__calcPoll()
        self.__calRSquare()
        
    def __sum(self):
        
        for i in range(self.m):
            
            self.sumColumn[i] = sum(self.matrix[:,i])
            
    def __sumSquare(self):
        
        for i in range(self.m):
            summ = 0
            for j in range(self.n):
                
                summ = summ + math.pow(self.matrix[j,i],2)
                
            self.sumColumnSquare[i] = summ
            
    def __calcPoll(self):
        
        self.poll = self.matrix.T.dot(self.matrix)
        
    def __calRSquare(self):
        
        for i in range(self.m):
            for j in range(i,self.m):
                
                result1 = (self.n * self.poll[i,j]) - (self.sumColumn[i] * self.sumColumn[j])
                result2 = (self.n * self.sumColumnSquare[i]) - math.pow(self.sumColumn[i],2)
                result3 = (self.n * self.sumColumnSquare[j]) - math.pow(self.sumColumn[j],2)
                
                r = result1 / math.sqrt(result2 * result3)
                
                self.rMatrix[i,j] = math.pow(r,2)
                self.rMatrix[j,i] = math.pow(r,2)
                
    def getRMatrix(self):
        
        return self.rMatrix
                                  