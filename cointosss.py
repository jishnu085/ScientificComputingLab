import random
from matplotlib.pyplot import *
N=[10,1000,100000]
R=[[],[],[]]
ER=[]
for j in range(len(N)):
    

    for i in range(N[j]):
        cointoss=random.randint(0,1)
        if(cointoss==0):
         R[j].append(1)
        else:
         R[j].append(0)

    x=(R[j].count(1))/N[j]
    y=abs(0.5-x)
    ER.append(y)
print(ER)

plot(N,ER)
show()


