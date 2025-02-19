from matplotlib.pyplot import *
from numpy import *
from odeint import *
x=arange(0,10,0.01)
subplot(3,3,1)
y=sin(x)
plot(x,y)
subplot(3,3,2)
y2=gradient(y)
plot(x,y2)
subplot(3,3,3)
y3=sinh(x)
plot(x,y3)
subplot(3,3,4)
y4=gradient(y3)
plot(x,y4)
show()
