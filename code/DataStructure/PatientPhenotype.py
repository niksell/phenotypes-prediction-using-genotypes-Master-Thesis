from DataStructure.Snp import Snp

class PatientPhenotype:
    
    def __init__(self, eid, case, sex, yearBirth):
        
        self.eid = eid.strip()
        self.case = int (case.strip())
        self.sex = sex.strip()
        self.yearBirth = yearBirth.strip()
        self.snps = {}
        
    def getEid(self):
        return self.eid
     
    def getCase(self):
        return self.case
    
    def getSex(self):
        return self.sex
    
    def getYearBirth(self):
        return self.yearBirth
        
    def addSnps(self, snpId, allele1,allele2):
        self.snps[snpId] = Snp(snpId,allele1,allele2)
        
    def snpCode(self,alleles = '', snp = '', code = -1):
    
        if code == -1:
                
            self.snps[snp.strip()].setSnpCode(alleles[0],alleles[1])
                    
        else:
            
            self.snps[snp.strip()].setCode(code)
            
    def getSnpCode(self,snpId):
        return self.snps[snpId].getSnpCode()
    
    def getAllele1(self,snpId):
        return self.snps[snpId].getAllele1()
    
    def getAllele2(self,snpId):
        return self.snps[snpId].getAllele2()
        
    def getSize(self):
        return len(self.snps)
        