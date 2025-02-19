import random
from numpy import *
from matplotlib.pyplot import *
# s=random.uniform(0,20,25)
# threshold=9
# crossed=count_nonzero(s>=threshold)
# print(crossed)
# k=random.randn(100)
# s=random.randn(100)
# scatter(k,s)
# show()
x=arange(0,10,0.0001)
y=sin(x)

plot(x,y,'-g',label="sinx")
legend()
show()