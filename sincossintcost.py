from matplotlib.pyplot import *
from numpy import *
from scipy.integrate import odeint
t=arange(0,10,0.1)
figure.figsize=(300,100)
x=sin(t)
subplot(4,4,1)
xlabel('time')
ylabel('sin')
figure.figsize=(30,10)
plot(t,x)

subplot(4,4,2)
x2=gradient(x)
xlabel('time')
ylabel('gradient of sin')
figure.figsize=(30,10)
plot(t,x2)

subplot(4,4,3)
x3=cos(t)
xlabel('time')
ylabel('cos')
figure.figsize=(30,10)
plot(t,x3)

subplot(4,4,4)
x4=gradient(x3)
xlabel('time')
ylabel('gradient of cos')
figure.figsize=(30,10)
plot(t,x4)

subplot(4,4,5)
x5=sinh(t)
xlabel('time')
ylabel('sinht')
plot(t,x5,label="sinht")
rcParams["figure.figsize"]=(30,10)
legend()

subplot(4,4,6)
x6=gradient(x5)
xlabel('time')
ylabel('gradofsinht')
figure.figsize=(30,10)
plot(t,x6,label="gofsinht")
legend()
show()


