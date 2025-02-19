from numpy import *
from scipy.integrate import odeint
from matplotlib.pyplot import *
def ordiff(x,t):
    dxdt=-((e**x)+(2*x))
    return dxdt

x0=1
t=arange(0,10,0.1)
k=odeint(ordiff,x0,t)
print(k)
plot(t,k)
show()