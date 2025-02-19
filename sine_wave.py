from  matplotlib.pyplot import *
from numpy import *

x = arange(0, 5*pi, 0.1)
y = sin(x)
grid(1)
plot(x, y, color='green')

show()