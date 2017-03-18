patients = open('phenotype_euro_edit.txt','r')
patientsBa = open('phenotype_euro_balanced2.txt','w')

case = 0 

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
		if control <= case + (case*20/100):
			if int (i.split()[3].strip()) == 1:
				print("ok1")
			patientsBa.write(i)
			control += 1
			lines += 1
			
	else:
		if int (i.split()[3].strip()) == 0:
			print("ok")
		patientsBa.write(i)
		lines += 1
	
print("controls = ",control-1)	
print("lines = ",lines)

patients.close()
patientsBa.close()


patientsBa.close()