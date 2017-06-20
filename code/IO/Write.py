import os.path
from DataStructure.PatientPhenotype import PatientPhenotype

class Write:
    
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
        
        path = self.__path + name
        
        if os.path.exists(path):
            print("the file already exists........ give another name")
            return
        
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
                    write.write("chromosome"+(i)+'\n')
                    for j in snps:
                        if j in chromosomes[chro]:
                            write.write(j + '\n')
                    write.write('\n')

            write.close()
        except Exception as x:
            print("error = ",x)
            write.close()
            
    def saveData(self,ids,patients,data,chroms = {}):
    
        self.__snpCodeLog(ids['patients']['idToName'],ids['snps']['idToName'],patients,data)
        
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