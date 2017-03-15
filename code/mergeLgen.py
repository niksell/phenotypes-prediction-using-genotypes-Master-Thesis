import os
for i in range(1,23):
	
	if os.path.exists('chr'+str(i)+'test.lgen'):
	
		test = open('chr'+str(i)+'test.lgen','r')
		train = open('chr'+str(i)+'train.lgen','r')
		lgen = open('chr'+str(i)+'.lgen','w')
	
		for line in test:
	
			lgen.write(line)
		
		for line in train:
	
			lgen.write(line)
		
		train.close()
		test.close()
		lgen.close()
		
		os.remove('chr'+str(i)+'test.lgen')
		os.remove('chr'+str(i)+'train.lgen')