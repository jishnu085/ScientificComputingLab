from numpy import *
coeffs=[3,0,0,0,5]
k=poly1d(coeffs)
j=polyder(k)
t=[-3,3]
d=j(t)
print(d[0])
print(d[1])