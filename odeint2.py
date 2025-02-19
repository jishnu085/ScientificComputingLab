from numpy import *
from matplotlib.pyplot import *
k=arange(-5,5,0.01)
x=4*(k**2)
plot(k,x,label="fn")
legend()
show()

y=gradient(x)
plot(k,y,label="2ndfn")
legend()
show()