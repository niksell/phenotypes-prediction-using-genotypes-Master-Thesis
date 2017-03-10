class SaveDataSet():
    def __init__(self,name,ids,data):
        
        self.name = name
        self.ids = ids
        self.data = data
        self.__writeLogFile()
        self.__writeVariables('patients')
        self.__writeVariables('snps')
        self.__writeCSV()
        
    def __writeLogFile(self):
        
        write = open(self.name+'.log','w')
        write.write("Log file for the Test Data Set "+self.name+'\n')
        write.write(self.name + " has "+ str(len(self.ids['patients']['nameToId'].keys())) + " patients "'\n')
        write.write(self.name + " has "+ str(len(self.ids['snps']['nameToId'].keys())) + " snps "'\n')
        write.close()
        
    def __writeVariables(self,kind):
        
        write = open(self.name+'_'+kind+'.txt','w')
        write.write(kind + '\n')
        
        for i in range(len(self.ids[kind]['nameToId'].keys())):
            name = self.ids[kind]['idToName'][i]
            write.write(name + '\t'+str(self.ids[kind]['nameToId'][name]) + '\n')
        
        write.close()
        
        
    def __writeCSV(self):
        
        try:
            
            with open(self.name+'.csv', 'w') as csvfile:
                writer = csv.writer(csvfile, dialect='excel', quoting=csv.QUOTE_NONNUMERIC)
            
                line = []
                for i in range(len(self.ids['snps']['nameToId'].keys())):
                   # if i == 0 :
                    #    line += self.ids['snps']['idToName'][i]
                    #else:
                    line.append(self.ids['snps']['idToName'][i])
                writer.writerow(line)
            
                line = [] 
                for i in range(len(self.ids['snps']['nameToId'].keys())):
                    name = self.ids['snps']['idToName'][i]
                 #   if i == 0:
                  #      line += str(self.ids['snps']['nameToId'][name])
                   # else:
                    line.append(str(self.ids['snps']['nameToId'][name]))
                writer.writerow(line)
            
            
                for i in range(len(self.ids['patients']['nameToId'].keys())):
                    line = []
                    for j in range(len(self.ids['snps']['nameToId'].keys())):
                        #if j == 0:
                        #    line += str(self.data[i,j]) 
                        #else:
                        
                        line.append(str(self.data[i,j]))
                        
                    writer.writerow(line)
        finally:
            pass   