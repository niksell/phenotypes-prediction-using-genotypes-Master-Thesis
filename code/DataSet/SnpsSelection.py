
def _counterSnps(n):
	snpsCount = {}
	for i in range(n):
		snpsCount[i] = 0
		
	return snpsCount
	
	
def _countSnps(X,b):

	snpsCount = _counterSnps(len(X.T))
		
	for i in range(len(X)):
	
		for j in range(i+1,len(X.T)):
			
			if X[i,j] - b >= 1e-10:
			
				snpsCount[i] = snpsCount[i] + 1
				snpsCount[j] = snpsCount[j] + 1
				
	return snpsCount
	

def highCorrelation(X, b, c):

	snpsRed = []
	count = 0
	
	snpsCount = _countSnps(X,b)
	
	for i in snpsCount.keys():
		if snpsCount[i] > c * len(X.T) / 100:
		
			snpsRed.append(i)
			count += 1
			
	print("count = ",count)
	print("len snpsRed = ",len(snpsRed))
	
def lowCorrelation(X, b, c):

	snpsRed = []
	count = 0
	
	snpsCount = _countSnps(X,b)
	
	for i in snpsCount.keys():
		if snpsCount[i] <= c * len(X.T) / 100:
			snpsRed.append(i)
			count += 1

	print("count = ",count)
	print("len snpsRed = ",len(snpsRed))
	
	return snpsRed



	