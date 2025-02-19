from numpy import *
from scipy import *
from pylab import *
a=array([[10,-3,-6],[-3,10,0],[-6,0,10]])
a2=inv(a)
b=array([[10],[-5],[25]])

c=dot(a2,b)
print(c)
print('the value of i1 is = ',c[0])
print('the value of i2 is = ',c[1])
print('the value of i3 is = ',c[2])
