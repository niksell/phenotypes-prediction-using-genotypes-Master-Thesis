patients = open('phenotype_euro_edit.txt','r')
patientsBa = open('phenotype_euro_balanced_train1.txt','w')

case = 0 
balanced = []

i = patients.readline()
patientsBa.write(i)

for i in patients:
	
	if int (i.split()[3].strip()) == 1:
		
		case += 1

patients.close()

print("cases = ",case)		

patients = open('phenotype_euro_edit.txt','r')	
patients.readline()

control = 1		
lines = 0
for i in patients:
	if int (i.split()[3].strip()) == 0:
		if control <= case :
			
			patientsBa.write(i)
			balanced.append(i.split()[0])
			control += 1
			lines += 1
			
	else:
		
		patientsBa.write(i)
		balanced.append(i.split()[0])
		lines += 1
	
print("controls = ",control-1)	
print("lines = ",lines)

patients.close()
patientsBa.close()

patients = open('phenotype_euro_edit.txt','r')	
patientsTest = open('phenotype_euro_test1.txt','w')

i = patients.readline()

patientsTest.write(i)
count = 0

for i in patients:

	if i.split()[0] not in balanced:
		count += 1
		patientsTest.write(i)

patients.close()
patientsTest.close