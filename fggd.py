from numpy import *
from matplotlib.pyplot import *
fs = 2000
t = arange(0,1,1/fs)
s = cos(2*pi*1*t) + 2*cos(2*pi*2*t) + 0.5*cos(2*pi*7*t)
x_k = fft.fft(s)
print(real(x_k))
t2 = arange(-fs, fs)
stem(t2, abs(x_k))