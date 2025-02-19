from numpy import *
from matplotlib.pyplot import *
s=random.uniform(0,10,50)
print(s)
plot(s)

vt=2
vt_p=full(s.shape,vt)
plot(vt_p)
show()
g_th=count_nonzero(s>=vt)
print(g_th)
print("no of values crossed threshold= ",g_th)