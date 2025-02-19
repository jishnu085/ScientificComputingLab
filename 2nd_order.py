from numpy import *
from scipy.integrate import odeint
from matplotlib.pyplot import *

def module(x,t):
    dx2dt=x[1],-2*x[1]-(2*(x[0])+exp(-t))
    return dx2dt

x0=[0,1]
t=linspace(0,10,100)
ys=odeint(module,x0,t)
k1=ys[:,0]
k2=ys[:,1]
print(k1)
print(k2)
plot(t,k1)
plot(t,k2)
show()
