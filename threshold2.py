from numpy import*
from matplotlib.pyplot import *
s=random.uniform(0,10,50)
plot(s)
vt=3
vt_p=full(s.shape,vt)
plot(vt_p)
g_th=count_nonzero(s>=vt)
print(g_th)
show()



from numpy import *
from matplotlib.pyplot import *
s=random.uniform(0,10,50)
plot(s)
vt=5
v_t=full(s.shape,vt)
plot(v_t)
show( )
g_th=count_nonzero(s>=vt)
print(g_th)