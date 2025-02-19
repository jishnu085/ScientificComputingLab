from numpy import *
from scipy.integrate import quad
def funcn(t):
    k=(4*(t**3))+(2*t)+3
    return k

inte,err=quad(funcn,0,2)
print('integral of the function is = ',inte)
print('aproximate error is = ',err)