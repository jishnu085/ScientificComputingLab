from numpy import *
from scipy.integrate import odeint
from matplotlib.pyplot import *
def sol(x,t):
    dxdt=-2*x
    return dxdt
x0=1
t=arange(0,10,0.00001)
y=odeint(sol,x0,t)
plot(t,y,)
show()