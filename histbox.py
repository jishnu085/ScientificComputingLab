from numpy import *
from matplotlib.pyplot import *
x=random.randint(0,10,1000)
t=arange(0,10,0.001)
print(x)
figure()
# hist(x)
box(x)
show()
threshold=2
s=count_nonzero(x<=threshold)
print(s)