from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import odeint

def model(X,t):
    dx2dt=[X[1],-2*X[1]-2*X[0]+exp(-t)]
    return dx2dt
X0=[0,1]
t=linspace(0,20,100)
Xs=odeint(model,X0,t)
Ys=Xs[:,0]
Ys1=Xs[:,1]
plot(t,Ys)
plot(t,Ys1)
show()