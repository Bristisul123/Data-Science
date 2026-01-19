from itertools import groupby
data=sorted('orangee')
for k,g in groupby(data): 
    print(k,list(g))