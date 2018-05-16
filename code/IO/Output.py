import os.path
import time
import numpy as np
from DataStructure.PatientPhenotype import PatientPhenotype
from DataStructure.Snp import Snp

class Output:
    
    def __init__(self,path,numberOfChromosomes):
        
        self.__path = path
        self.__numberOfChromosomes = numberOfChromosomes
        
    def writePatientsList(self,patients,kind):
        
        path = self.__path + kind
        
        try:
            write = open(path,'w')
            for patient in patients.keys():
                write.write(patient.strip() + '\n')
            
            write.close()
        except Exception as x:
            print("error = ",x)
            write.close()
        
        
    def writeSnpsList(self,chromosomes):
        
        for i in range(self.__numberOfChromosomes):
    
            chro = 'chr'+str(i+1)
            try:
                path = self.__path + chro + 'snpList.txt'
                write = open(path,'w')

                for snp in chromosomes[chro].keys():
                    write.write(snp.strip() + '\n')

                write.close()
            except Exception as x:
                print("error = ",x)
                write.close()
            
    def writeSnpsUsed(self,snpsIds,idToName,chromosomes,name = None):
        
        if not name:
            print("give a name to file")
            return
        
        path = self.__path + name  + " ( " + time.strftime("%d-%m-%Y") + " ).txt "  
    
        i=1
        while os.path.exists(path):
            
            path = self.__path + name  + " ( " + time.strftime("%d-%m-%Y") + " ) " + '_' + str(i)+".txt"
            i += 1
        
        snps = []
        for i in snpsIds:
            snps.append(idToName[i])
            
        print("snpsIds = ",len(snpsIds))
        print("idToName = ",len(idToName))
        
        write = open(path,'w')
        try:
            for i in range(1,23):
            
                chro = 'chr'+str(i)
                chromList = chromosomes[chro]

                if len(list(set(chromList) - set(snps))) < len(chromList):
                    write.write("chromosome"+str(i)+'\n')
                    for j in snps:
                        if j in chromosomes[chro]:
                            write.write(j + '\t' + chromosomes[chro][j][0] + '\t' + chromosomes[chro][j][1] + '\n')
                    write.write('\n')

            write.close()
        except Exception as x:
            print("error = ",x)
            write.close()
            
    def saveData(self,ids,patients,data,chroms = {}):
    
        self.__snpCodeLog(ids['patients']['idToName'],ids['snps']['idToName'],patients,data)
        
    def writeDf(self,n,m,chromosomes,ids,patients):
        
        X = np.zeros((n,m),dtype = int)
       
        for i in range(self.__numberOfChromosomes):
            
            chro = 'chr'+str(i+1)
            path = self.__path + chro +'.lgen'
            
            
            
            if os.path.exists(path):
                
                try:
                    f = open(path,'r')
                    
                    for line in f:
                        try:
                             
                            patient = line.split()[0].strip()
                            snp = line.split()[2].strip()
                            allele1 = line.split()[3].strip()
                            allele2 = line.split()[4].strip()
                           
                            snpp = Snp(snp,allele1,allele2)
                            snpp.setSnpCode(chromosomes[chro][snp][0],chromosomes[chro][snp][1])
                            code = snpp.getSnpCode()
                            
                            p = ids['patients']['nameToId'][patient]
                            s = ids['snps']['nameToId'][snp]
                            
                            X[p,s] = code
                          
                        except Exception as x:
                            
                            print("error1 = ",x)
                            f.close()
                              
                    f.close()
              
                except Exception as x:
                        print("error2 = ",x)
                        f.close()
        
        print("x shape is ", X.shape)
        write = open(self.__path + 'snpCodeTest1.csv','w')
        
        write.write('patients,')
        
        for i in range(len(X.T)):
            
            s = ids['snps']['idToName'][i]
            write.write(s + ',')
            
        write.write('label' + '\n')
        
        for i in range(len(X)):
            
            p = ids['patients']['idToName'][i]
            write.write(p + ',')
                            
            for j in range(len(X.T)):
                
                s = ids['snps']['idToName'][j]
                write.write(str(X[i,j]) + ',')
                
            write.write(str(patients[p].getCase()) + '\n')
                        
                
        write.close()
        
        
        
    def __patientsLogFile(self,ids,patientKind):
        
        write = open(self.__path + patientKind + 'Ids.txt','w')
        
        write.write(str(len(ids['nameToId'])) + '\n')
        
        for patient in ids['nameToId'].keys():
            
            write.write(patient.strip() + '\t' + str(ids['nameToId'][patient]).strip() + '\n')
            
        write.close()
        
    def __snpsLogFile(self,ids,chroms):
        
        if len(chroms.keys()) > 0:
        
            write = open(self.__path + 'SnpsIds.txt','w')
        
            write.write(str(len(ids['nameToId'])) + '\n')
        
            for chro in chroms.keys():
              
                for snp in chroms[chro].keys():
                    write.write(snp.strip() + '\t' + str(ids['nameToId'][snp.strip()]).strip() + '\n')
            
            write.close()
            
    def __snpCodeLog(self,patientsIds,snpsIds,patients,data):
        
        write = open(self.__path + 'snpCode.txt','w')
        
        write.write(str(len(patientsIds)) + '\n')
        write.write(str(len(snpsIds)) + '\n')
        
        for i in range(len(data)):
            for j in range(len(data.T)):
                allele1 = patients[patientsIds[i]].getAllele1(snpsIds[j])
                allele2 = patients[patientsIds[i]].getAllele2(snpsIds[j])
                write.write(patientsIds[i].strip() + '\t' + snpsIds[j].strip() + '\t' + str(data[i,j]).strip() + '\t' 
                                                                            + allele1.strip() + '\t' + allele2.strip() + '\n')
                
        write.close()