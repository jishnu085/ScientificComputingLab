from scipy.integrate import quad
from matplotlib.pyplot import *
from numpy import *

def integ(x):
    return 2*(x**2)
ans=quad(integ,0,2*pi)
print(ans)