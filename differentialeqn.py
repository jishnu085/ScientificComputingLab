from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

def diff(x,t):
    dxdt=-2*x
    return dxdt
x0=1
t=linspace(0,20,50)
x=odeint(diff,x0,t)
plot(t,x)
show()