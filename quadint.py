from scipy.integrate import quad
from numpy import * 
def integral(t):
    return (4*t**2)+3
answer ,error=quad(integral,-2,2)
print("integral is  ",answer)
print("error= ",error)
def integ(k):
    return sin(k)
ans,err=quad(integ,0,(pi/2))
print("integral is  ",ans)
