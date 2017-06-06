class Snp:
    
    def __init__(self,snpId,allele1,allele2):
        
        self.snpId = snpId
        self.allele1 = allele1
        self.allele2 = allele2
        self.snpCode = -1
        self.snpCode1 = -1
        
    def getId(self):
        
        return self.snpId
        
    def getAllele1(self):
        
        return self.allele1
        
    def getAllele2(self):
        
        return self.allele2
        
    def setSnpCode(self,allele1,allele2):
      
        if self.allele1.strip() == allele1.strip() and self.allele2.strip() == allele1.strip():
            code = 2
           
        elif self.allele1.strip() == allele1.strip() and self.allele2.strip() != allele1.strip():
            code = 1
           
        elif self.allele1.strip() != allele1.strip() and self.allele2.strip() == allele1.strip():
            code = 1
            
        elif self.allele1.strip() != allele1.strip() and self.allele2.strip() != allele1.strip():
            code = 0
            
        self.snpCode = code
        
        
    def setSnpCode1(self,allele1,allele2):
        
        l1 = [allele1,allele2]
        l2 = [self.allele1.strip(),self.allele12.strip()]
        
        l1 = list(sorted(l1))
        l2 = list(sorted(l2))
      
        if self.allele1.strip() == allele1.strip() and self.allele2.strip() != allele2.strip():
            code = 1
           
        elif self.allele1.strip() == allele1.strip() and self.allele2.strip() == allele2.strip():
            code = 0
            
        elif self.allele1.strip() != allele1.strip() and self.allele2.strip() == allele2.strip():
            code = -1
            
        self.snpCode1 = code
        
    def setCode(self,aCode):
        
        self.snpCode = aCode
        
    def getSnpCode(self):
        
        return self.snpCode