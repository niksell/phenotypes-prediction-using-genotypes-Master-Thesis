import os.path
from DataStructure.PatientPhenotype import PatientPhenotype 

class Read:
    def __init__(self,path,numberOfChromosomes):
        
        self.__chromosomes = {}
        self.__numberOfSnps = 0
        self.__path = path
        self.__numberOfChromosomes = numberOfChromosomes
        
    def readPatients(self,kind):
        
        patients = {}
        
        try:
            f = open(self.__path + kind,'r')
            f.readline()
            
            
            try:

                for line in f:
                    patients[line.split()[0].strip()] = PatientPhenotype(line.split()[0],line.split()[3],
                                                                         line.split()[1],line.split()[2])
                    
                f.close()

            except Exception as x:
                print("error = ",x)
                f.close()
                
        except Exception as x:
            
            print("error = ",x)
            f.close()
        
        return patients
        
    
    def readSnps(self,fileKind):
        
        for i in range(self.__numberOfChromosomes):
    
            chro = 'chr'+str(i+1)
            path = self.__path + chro + fileKind
            
            try:
                
                f = open(path,'r')
                f.readline()
                
                try:

                    self.__chromosomes[chro] = self.__readSnpsOfChromosome(f)

                    f.close()

                except Exception as x:
                    print("error = ",x)
                    f.close()
                    
            except Exception as x:
            
                print("error = ",x)
                f.close()
                
    
                
        return self.__chromosomes
    
    def __readSnpsOfChromosome(self,file):
        
        snps = {} 
       
        for line in file:
            
            alleles = []
            alleles.append(line.split()[3].strip())
            alleles.append(line.split()[6].strip())
            
            try:
                if line.split()[1].strip() != '.':
                    snps[line.split()[1].strip()] = alleles
                    self.__numberOfSnps += 1
                    
            except Exception as x:
                print("error = ",x)
                
                file.close()
                
        return snps
        
    def readLgen(self,patients,kind = ''):
        
        
        for i in range(self.__numberOfChromosomes):
            
            chro = 'chr'+str(i+1)
            path = self.__path + chro + kind +'.lgen'
    
            if os.path.exists(path):
                
                try:
                    f = open(path,'r')
                
                    for line in f:
                        try:
                            if line.split()[0].strip() in patients.keys():

                                patients[line.split()[0].strip()].addSnps(line.split()[2].strip(),line.split()[3].strip(),
                                                                                        line.split()[4].strip())
                        except Exception as x:
                            print("error = ",x)
                            f.close()
                            
                    f.close()
              
                except Exception as x:
                        print("error = ",x)
                        f.close()
                
       
        return patients
    
    def getListOfSnps(self):
        snps = []
        for i in range(self.__numberOfChromosomes):
            chro = 'chr'+str(i+1)
            for snp in self.__chromosomes[chro].keys():
                snps.append(snp)
        
        return snps
        
    def getNumberOfSnps(self):
        
        return self.__numberOfSnps
    
    
    def readSnpsCode(self,patients,kind = ''):
        
        try:
            read = open(self.__path + kind + 'snpCode.txt','r')
            read.readline()
            read.readline()
            print("mphka2")
            for line in read:   

                try:
                    patient = line.split('\t')[0].strip()
                    snp = line.split('\t')[1].strip()
                    code = int (line.split('\t')[2].strip())
                    allele1 = line.split('\t')[3].strip()
                    allele2 = line.split('\t')[4].strip()
                    if patient in patients.keys() and snp != '.':
                        patients[patient].addSnps(snp,allele1,allele2)
                        patients[patient].snpCode(snp = snp,code = code)
                except Exception as x:
                    print("error = ",x)
                    read.close()
            
            read.close()
    
        except Exception as x:
            print("error = ",x)
            read.close()
            
        return patients
            