from scipy.integrate import *
from numpy import *
from matplotlib.pyplot import *
t=linspace(0,10,100)
def odeee(x,t):
    dxdt=-2*x+99
    return dxdt
x0=5
s=odeint(odeee,x0,t)
plot(t,s)
show()