from numpy import *
from matplotlib.pyplot import *
figure(figsize=(18, 5))
t=arange(0,10,0.001)
subplot(1,3,1)
f1=cos(t)
plot(t,f1)
subplot(1,3,2)
f2=cos(5*t)
plot(t,f2)
subplot(1,3,3)
f3=(f1*f2)+f2
plot(t,f3)
show()