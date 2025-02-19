from numpy import *
from scipy import *
from pylab import *
x=array([[3,2,-5],[1,-3,2],[5,-1,4]])
z=array([12,-13,10])
k=inv(x)
y=dot(k,z)
print('the value of x is = ',round(y[0],2))
print('the value of x is = ',round(y[1],2))
print('the value of x is = ',round(y[2],2))
print(det(x))
print(transpose(x))
print(dot(k,det(x)))
print(matrix_rank(x))
print(eig(x))
