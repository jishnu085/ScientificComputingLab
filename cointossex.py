import random
from matplotlib.pyplot import *

def cointoss(numbers):
    recordlist=[[],[],[],[],[],[]]
    errorlist=[[],[],[],[],[],[]]
    for i in range(0,6):
        for j in range(numbers[i]):
            flip=random.randint(0,1)
            if flip==0:
              
                recordlist[i].append(0)
            else:
        
                recordlist[i].append(1)
        probhead=recordlist[i].count(1)/numbers[i]
        error=0.5-probhead
        errorlist[i].append(abs(error))
    return errorlist   
numbers=[10,100,1000,10000,100000,1000000]
x=cointoss(numbers)
plot(x,numbers)
show()
        



