from numpy import *
from matplotlib.pyplot import *
t=linspace(0,10,50)

v0=5
vt=v0*(1-(exp(-t/3)))
print(vt)
plot(t,vt,label='voltage')
legend()
show()
