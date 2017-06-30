
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
    
    return snpsRed

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

#def union(xMatrix, yMatrix, corMartrix, b, c):
    
    
    
    
    
    
    
    
    