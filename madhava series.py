from numpy import *
from matplotlib.pyplot import*


n=0
N=1000
sum=0
error=[]
t=linspace(0,100,1000)

while(n<N):
    
    funct=((-1)**n)/((2*n)+1)
    sum=sum+funct
    n=n+1
    k=4*sum
    ab=pi-k
    error.append((ab))


print(error)
plot(t,error)
show()
