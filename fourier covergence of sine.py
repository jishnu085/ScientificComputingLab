from numpy import *
from matplotlib.pyplot import *
n=0
sum=0
x=linspace(0,10,1000)
figure(figsize=(10, 6))
while(n<=10000):
    funct=sin(((2*n)+1)*x)/(((2*n)+1))
    sum=sum+funct
    n=n+1

plot(x,sum)
tight_layout()
show()