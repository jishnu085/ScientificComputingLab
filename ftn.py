from matplotlib.pyplot import *
from numpy import *
from odeint import *
x=arange(-5,5,0.1)
subplot(2,2,1)
y=(4*x**2)+3
plot(x,y)
subplot(2,2,2)
y2=gradient(y)
plot(x,y2)
show()