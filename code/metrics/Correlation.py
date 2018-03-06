import numpy as np
import math
import DataSet.SnpsSelection as s

class Correlation():
    
	def __init__(self,X):
        
		self.__n = len(X)
		self.__m = len(X.T)
		self.__matrix = X
		self.__meanMatrix = np.zeros((self.__m,1))
		self.__covMatrix = None
		self.__correlationMatrix = np.zeros((self.__m,self.__m),dtype = float)
		self.__varMatrix = np.zeros((self.__m),dtype = float)
		self.__normalizedMatrix = np.zeros((self.__n,self.__m),dtype = float)
        
		self.__calculateMeanMatrix()
		self.__normalizeMatrix()
		self.__calculateCovMatrix()
		self.__calculateVar()
		self.__calclulateCorr()
        
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
       
		self.__covMatrix = (self.__normalizedMatrix.T.dot(self.__normalizedMatrix)) / (self.__n - 1)
        
        
	def __calculateVar(self):
        
		for i in range(self.__m):
            
			self.__varMatrix[i] = math.sqrt((self.__normalizedMatrix[:,i].dot(self.__normalizedMatrix[:,i])) / (self.__n-1 )) 
    
	def __calclulateCorr(self):
        
		for i in range(self.__m):
            
			for j in range(i,self.__m):
			
				result1 = self.__covMatrix[i,j]
				result2 = self.__varMatrix[i]
				result3 = self.__varMatrix[j]
				result = result1 / (result2 * result3)
				
				self.__correlationMatrix[i,j] = result
				self.__correlationMatrix[j,i] = result
				
	def getCorrMatrix(self):
	
		return self.__correlationMatrix
		
	
	def getLowCorrelationSnps(self, b, c = 0, up = 100, down = 0):
		
		return s.lowCorrelation(self.__correlationMatrix, b, c, up, down)
		
	def getHighCorrelationSnps(self, b, c = 0,up = 100, down = 0):
	
		return s.highCorrelation(self.__correlationMatrix, b, up, down)
	
		