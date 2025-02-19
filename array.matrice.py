from numpy import *
from matplotlib.pyplot import *
x=arange(0,10,0.1)
xlabel('time')
ylabel('sinx,cosx')
title('sinx and cosx plot')
legend(['sin(x)','cos(x)'])
y=sin(x)
z=cos(x)
plot(x,y,label='sinx')
plot(x,z,label='cosx')
legend()
show()