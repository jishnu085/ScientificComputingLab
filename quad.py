from numpy import *
from scipy.integrate import quad
from matplotlib.pyplot import *
def integral(t):
    x=4*(t**2)+3
    return x
ans,err=quad(integral,-2,2)
print('the integral of the function is = ',ans)
print('estimate of the absolute error is= ',err)