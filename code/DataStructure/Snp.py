class Snp:
    
    def __init__(self,snpId,allele1,allele2):
        
        self.__snpId = snpId
        self.__allele1 = allele1
        self.__allele2 = allele2
        self.__snpCode = -1
        self.__snpCode1 = -1
        
    def getId(self):
        
        return self.__snpId
        
    def getAllele1(self):
        
        return self.__allele1
        
    def getAllele2(self):
        
        return self.__allele2
        
    def setSnpCode(self,allele1,allele2):
      
        if self.__allele1.strip() == allele1.strip() and self.__allele2.strip() == allele1.strip():
            code = 2
           
        elif self.__allele1.strip() == allele1.strip() and self.__allele2.strip() != allele1.strip():
            code = 1
           
        elif self.__allele1.strip() != allele1.strip() and self.__allele2.strip() == allele1.strip():
            code = 1
            
        elif self.__allele1.strip() != allele1.strip() and self.__allele2.strip() != allele1.strip():
            code = 0
            
        self.__snpCode = code
        
        
    def setSnpCode1(self,allele1,allele2):
        
        l1 = [allele1,allele2]
        l2 = [self.__allele1.strip(),self.__allele12.strip()]
        
        l1 = list(sorted(l1))
        l2 = list(sorted(l2))
      
        if self.__allele1.strip() == allele1.strip() and self.__allele2.strip() != allele2.strip():
            code = 1
           
        elif self.__allele1.strip() == allele1.strip() and self.__allele2.strip() == allele2.strip():
            code = 0
            
        elif self.__allele1.strip() != allele1.strip() and self.__allele2.strip() == allele2.strip():
            code = -1
            
        self.__snpCode1 = code
        
    def setCode(self,aCode):
        
        self.__snpCode = aCode
        
    def getSnpCode(self):
        
        return self.__snpCode