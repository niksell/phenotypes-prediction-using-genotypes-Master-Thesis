
def _counterSnps(n):
    snpsCount = {}
    for i in range(n):
        snpsCount[i] = 0
    
    return snpsCount


def _highClass(X,b,c):

    snpsCount = _counterSnps(len(X.T))

    for i in range(len(X)):

        for j in range(i+1,len(X.T)):

            if X[i,j] - b > 1e-10 and X[i,j] >= c:

                snpsCount[i] = snpsCount[i] + 1
                snpsCount[j] = snpsCount[j] + 1

    return snpsCount

def _lowClass(X,b,c):

    snpsCount = _counterSnps(len(X.T))

    
    for i in range(len(X)):

        for j in range(i+1,len(X.T)):

            if X[i,j] - b <= 1e-10 and X[i,j] >= c:
            
                snpsCount[i] = snpsCount[i] + 1
                snpsCount[j] = snpsCount[j] + 1
            
            
    return snpsCount


def _findCaseControl(y):
    
    cases = []
    controls = []
    

              
    for i in range(len(yTraining1)):
        if y[i] == 0 :
            controls.append(i)

        elif y[i] == 1:
            cases.append(i)
            
            
    return cases,controls

def _findIdsOfPatients(aList):
    
    ids = {}
    count = 0
    
    for i in aList:
        ids[i] = count
        
        count += 1

def _seperateControlsCases(x,y):
    

    cases,controls = _findCaseControl(y)
    
    control = np.zeros((len(controls),len(xTraining.T)))
    case = np.zeros((len(cases),len(xTraining.T)))
    
    idsCo = _findIdsOfPatients(controls)
    idsCa = _findIdsOfPatients(cases)
    
    for i in controls:
        pos = idsCo[i]
        control[pos,:] = x[i,:]
      
    for i in cases:
        pos = idsCa[i]
        case[pos,:] = x[i,:]

    print("cases = ",case.shape)
    print("controls = ",control.shape)

    return case, control


def highCorrelation(X, b, c, up,down):

    snpsRed = []
    count = 0
    
    snpsCount = _highClass(X,b,c)

    for i in snpsCount.keys():
        if snpsCount[i] >= down * (len(X.T)-1) / 100 and snpsCount[i] <= up * (len(X.T)-1) / 100:

            snpsRed.append(i)
            count += 1

    print("count = ",count)
    print("len snpsRed = ",len(snpsRed))
    
    return snpsRed

def lowCorrelation(X, threshold = 0.7, c = -2, up = 100,down = 100):

    snpsRed = []
    count = 0
    
    snpsCount = _lowClass(X,threshold,c)
    
    for i in snpsCount.keys():
        
        if snpsCount[i] >= down * (len(X.T)-1) / 100 and snpsCount[i] <= up * (len(X.T)-1) / 100:
            snpsRed.append(i)
            count += 1

    print("count = ",count)
    print("len snpsRed = ",len(snpsRed))

    return snpsRed

def getTheNSemanticSnps(X, n = 30, c = -2, threshold = 0.7):
    
    snpsRed = {}
   
    snpsCount = _lowClass(X,threshold,c)
    
    snps = {}
    
    for i in snpsCount.keys():
      
        key = snpsCount[i]
        snps[key]=[]
        
    for i in snpsCount.keys():
        
        key = snpsCount[i]
        snps[key].append(i)
        
    snpss = list(snps.keys())
    
    sc = sorted(snpss,reverse=True)
    
    print("sc max to min is ",sc)
        
    for i in range(30):
        
        key = sc[i]
        snp = snps[key][0]
        snps[key].remove(0)
        snpsRed[snp] = key
        
    return snpsRed
    
    
    
    
    
    
    
    
    
