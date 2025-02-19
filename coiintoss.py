# import random
# from matplotlib.pyplot import *
# N=[100,500,1000,5000,10000,50000]
# absoluterror=[]
# for j in N:
    
#     result=[]
#     for i in range (j):
        
#         cointoss=random.randint(0,1)
#         if(cointoss==0):
#             result.append(1)
#         else:
#             result.append(0)
#     ph=result.count(1)/j
        
#     absrr=abs(0.5-ph)
#     absoluterror.append(round(absrr,3))

# print(absoluterror)
# plot(N,absoluterror)
# show()
import random
from matplotlib.pyplot import *
n=[100,200,500,1000,50000]
absoluterror=[]
for j in n:
    result=[]
    for i in range(j):
        cointoss=random.randint(0,1)
        if(cointoss==0):
            result.append(1)
        else:
            result.append(0)
    ph=result.count(1)/j
    absr=abs(0.5-ph)
    absoluterror.append(round(absr,3))  

print(absoluterror)
plot(n,absoluterror)
show()

            




 


