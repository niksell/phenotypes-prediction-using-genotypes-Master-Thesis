test = open('testSnpCode.txt','r')
train = open('trainSnpCode.txt','r')
merge = open('snpCode.txt','w')

for i in test:
	merge.write(i)
train.readline()
train.readline()	
for i in train:
	merge.write(i)
	
train.close()
merge.close()
test.close()