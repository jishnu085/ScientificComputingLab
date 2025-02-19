from numpy import *
from matplotlib.pyplot import *
n=99999
s=0
x=linspace(0,10,200)
for i in range(n):
    s=s+sin(((2*i)+1)*x)/((2*i)+1)
    


plot(x,s)
show()