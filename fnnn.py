from numpy import *
from matplotlib.pyplot import *
from scipy.integrate import quad

# t=arange(-5,5,0.01)
# f=((4*t)**2)+3
# plot(t,f)
# show()

# def module (t):
#     return 4*(t**2)+3
     
# y=quad(module,-2,2)

# print(y)


def fii(x):
  return  1/(sqrt(2)*pi*exp(-x**2))
x=quad(fii,0,Infinity)
print(x)