import numpy as np

class PCA:
    
    def __init__(self,X,error = 0.9):
        
    
        self.__matrix = X
        self.__n = len(X)
        self.__m = len(X.T)
        self.__eigenValues = None
        self.__eigenVectors = None
        self.__F = None
        self.__F1 = None
        self.__finalData = None
        self.__selectedSnps = []
        self.__eigenValuesPos = {}
        self.__kEigenVectors = 0
        self.__error = error
        self.__meanMatrix = np.zeros((self.__m,1),dtype = float)
        self.__normalizedMatrix = np.zeros((self.__n,self.__m),dtype = float)
        self.__covMatrix = None
        
        self.__calculateMeanMatrix()
        self.__normalizeMatrix()
        self.__calculateCovMatrix()
        self.__calculateEigenValuesAndEigenVectors()
        self.__findKEigenVectors()
        self.__createFMatrix()
        self.__createFinalMatrix()
                                  
    def __calculateMeanMatrix(self):
        
        for i in range(self.__m):
            summ = 0
            for j in range(self.__n):
                summ = self.__matrix[j,i] + summ
                
            self.__meanMatrix[i] = summ / self.__n
            
    def __normalizeMatrix(self):
        
        for i in range(self.__m):
            
            for j in range(self.__n):
                
                self.__normalizedMatrix[j,i] = self.__matrix[j,i] - self.__meanMatrix[i] 
            
    def __calculateCovMatrix(self):
       
        self.__covMatrix = (self.__normalizedMatrix.T.dot(self.__normalizedMatrix)) / (self.__n-1)
     #   print("cov = ",self.__covMatrix)

    def __calculateEigenValuesAndEigenVectors(self):
        
        eigen = np.linalg.eigh(self.__covMatrix)
        self.__eigenValues = eigen[0]
        self.__eigenVectors = eigen[1]
            
        for i in self.__eigenValues:
            self.__eigenValuesPos[i] = []
            
        for i in range(len(self.__eigenValues)):
            self.__eigenValuesPos[self.__eigenValues[i]].append(i)
            
       # print("values = ",self.__eigenValues)
       # print("pos1 = ",self.__eigenValuesPos[self.__eigenValues[0]])
            
        self.__eigenValues = sorted(self.__eigenValues,reverse = True)
        #print("values after = ",self.__eigenValues)
        #print("pos2 = ",self.__eigenValuesPos[self.__eigenValues[0]])
            
    def __findKEigenVectors(self):
        
        
        sumOfEigenValues = sum(self.__eigenValues)
        summ = 0
        count = 0
        
        while (summ / sumOfEigenValues) - self.__error < 1e-10:
            
            summ = summ + self.__eigenValues[count]
            count += 1
            
    #    print("count is ",count)
    #    print("sum of eigenValues = ",sumOfEigenValues)
    #    print("sum is ",summ)
        
        self.__kEigenVectors = count
            
    def __createFMatrix(self):
        
        self.__F = np.zeros((self.__m,self.__kEigenVectors),dtype = float)
        
        
        for i in range(self.__kEigenVectors):
            
            pos = self.__eigenValuesPos[self.__eigenValues[i]][0]
            self.__selectedSnps.append(pos)
            self.__eigenValuesPos[self.__eigenValues[i]].remove(pos)
            
            self.__F[:,i] = self.__eigenVectors[:,pos]
        
        
        self.__eigenValues = np.array(self.__eigenValues)
        self.__F1 = self.__eigenValues[:self.__kEigenVectors].T.dot(self.__F.T)
        
        print("f = ",self.__F.shape)
        print("f1 = ",self.__F1.shape)
                
        
    def __createFinalMatrix(self):
        
        self.__finalData = self.__matrix.dot(self.__F)
        
        
    def getSelectedSnps(self):
        
        return self.__selectedSnps
            
    def getFinalData(self,matrix = None):
        
        if matrix == None:
            
            return self.__finalData
        
        else:
            
            return matirx.dot(self.__F)
        
        
    def predict(self,X):
        
        predictList = []
            
        for i in range(len(X)):
            print("x = ",X.shape)
            result = X[i,:].dot(self.__F1.T)
            predictList.append(result)
            
        return predictList
        
        
        
        
        
        
        
        
        
        
        