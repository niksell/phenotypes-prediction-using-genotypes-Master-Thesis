test = open('testSnpCode.txt','r')
train = open('trainSnpCode.txt','r')
merge = open('snpCode.txt','w')

n = int (train.readline())
m = train.readline()

n += int (test.readline())
test.readline()

merge.write(str(n) + '\n')
merge.write(m)

for i in test:
	merge.write(i)
	
for i in train:
	merge.write(i)
	
train.close()
merge.close()
test.close()