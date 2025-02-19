from numpy import *
from matplotlib.pyplot import *
t=arange(0,10,0.01)
y= sin(t)
y1=gradient(y)
plot(t,y)
plot(t,y1)

title('SineWAve')
xlabel('Time')
ylabel('Amplitude')
show()