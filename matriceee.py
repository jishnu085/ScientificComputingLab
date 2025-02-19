from numpy import *
from matplotlib.pyplot import *
from pylab import *
x=array([1+9j,2,-3,7,8,-9])
for i in range(len(x)):
   print(x[i]) 
   print(x[i].real)
   print(x[i].imag)
   print(abs(x[i]))
y=array([1,2,3,4,1,6,7,8])
z=array([8,7,6,5,1,3,2,1])  
subplot(2,1,1)  


subplot(2,1,2)

show()
k=mat([[1,5,3],[1,5,9],[7,8,9]])
print(k)
print(shape(k))
print(transpose(k))
print(inv(k))
print(matrix_rank(k))
print(eig(k))
print(det(k))

