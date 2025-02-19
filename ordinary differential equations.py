from numpy import *
from scipy.integrate import odeint
from matplotlib.pyplot import *
def diff(x,t):
    dxdt=-2*x
    return dxdt
x0=5  
t=arange(0,20,1)
s=odeint(diff,x0,t)
plot(t,s)
show()