import os 

patients = open('Patients.txt','r')
file = 'Patients_Balanced.txt'
name = 0

while os.path.exists(file):
	name+=1
	file = 'Patients_Balaned'+str(name)+'.txt'

patientsBa = open(file,'w')

case = 0
balanced = []

i = patients.readline()
patientsBa.write(i)

for i in patients:

	if int (i.split()[3].strip()) == 1:

		case += 1

patients.close()

print("cases = ",case)

patients = open('Patients.txt','r')
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

	elif int (i.split()[3].strip()) == 1:
		
		patientsBa.write(i)
		
patients.close()
patientsBa.close()

