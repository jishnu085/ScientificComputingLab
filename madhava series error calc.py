from numpy import *
from matplotlib.pyplot import *
N=[10,100,500,1000,10000]
error=[]
for j in N:
    sum=0
    for i in range(j):
        fn=((-1)**i)/((2*i)+1)
        sum=sum+fn
    suum=(4*sum)
    er=abs(pi-suum)
    error.append(er)

print(error)
plot(N,error)
show()