from numpy import *
from matplotlib.pyplot import *
import pylab
x=[[1,9,3],[4,5,4],[7,2,9]]
print(transpose(x))
print(shape(x))
print(linalg.inv(x))
print(linalg.det(x))
print(linalg.eig(x)) 
t=linspace(0,10,10)
y=t**3
k=random.rand(10)
xlabel('function')
ylabel('time')
plot(t,y)
stem(t,y)
scatter(k,y)

show()