from numpy import *
from matplotlib.pyplot import *
t=arange(0,10,0.01)
figure.figsize=(100,6)
subplot(3,3,1)
xlabel('time')
ylabel('amplitude')
y=sin(t)
plot(t,y,label='sin(t)')
subplot(3,3,2)
figure.figsize=(100,6)
xlabel('time')
ylabel('amplitude')
y1=cos(t)
plot(t,y,label='cos(t)')
subplot(3,3,3)
xlabel('time')
ylabel('amplitude')
y2=gradient(y)
plot(t,y2,label='cos(t)')
legend()
subplot(3,3,4)
xlabel('time')
ylabel('amplitude')
y3=gradient(y1)
plot(t,y3,label='-sin(t)')
subplot(3,3,5)
y4=2*sin(t)*cos(t)*cos(5*t)
plot(t,y4,label='fn1')
legend()
subplot(3,3,6)
y5=cos(5*t)*cos(t)+cos(t)
plot(t,y5,label='fn2')
legend()
show()




