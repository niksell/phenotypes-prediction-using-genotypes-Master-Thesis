import numpy as np
import math

class RSquare():
    
    def __init__(self,X):
        
        self.__matrix = X
        self.__n = len(X)
        self.__m = len(X.T)
        self.__sumColumn = np.zeros((self.__m))
        self.__sumColumnSquare = np.zeros((self.__m))
        self.__poll = None
        self.__rMatrix = np.zeros((self.__m,self.__m))
        
        self.__sum()
        self.__sumSquare()
        self.__calcPoll()
        self.__calRSquare()
        
    def __sum(self):
        
        for i in range(self.__m):
            
            self.__sumColumn[i] = sum(self.__matrix[:,i])
            
    def __sumSquare(self):
        
        for i in range(self.__m):
            summ = 0
            for j in range(self.__n):
                
                summ = summ + math.pow(self.__matrix[j,i],2)
                
            self.__sumColumnSquare[i] = summ
            
    def __calcPoll(self):
        
        self.__poll = self.__matrix.T.dot(self.__matrix)
        
    def __calRSquare(self):
        
        for i in range(self.__m):
            for j in range(i,self.__m):
                
                result1 = (self.__n * self.__poll[i,j]) - (self.__sumColumn[i] * self.__sumColumn[j])
                result2 = (self.__n * self.__sumColumnSquare[i]) - math.pow(self.__sumColumn[i],2)
                result3 = (self.__n * self.__sumColumnSquare[j]) - math.pow(self.__sumColumn[j],2)
                
                r = result1 / math.sqrt(result2 * result3)
                
                self.__rMatrix[i,j] = math.pow(r,2)
                self.__rMatrix[j,i] = math.pow(r,2)
                
    def getRMatrix(self):
        
        return self.__rMatrix
                                  