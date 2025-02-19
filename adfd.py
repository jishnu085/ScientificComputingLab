from numpy import *
from matplotlib.pyplot import *
import time
dft_times =[]
values=[]
fft_times =[]
def dft_matrix(N):
    n = arange(N)
    k = n[:,None]
    omega = exp(-2j*pi*k*n/N)
    return omega

def fft_matrix(N):
    X = random.rand(N)
    Y = fft.fft(X)
    return Y

def calc_time(N):
    start_time = time.time()
    dft_matrix(N)
    stop_time = time.time()
    total_time = stop_time-start_time
    dft_times.append(total_time)
    start_time = time.time()
    fft_matrix(N)
    stop_time = time.time()
    total_time = stop_time-start_time
    fft_times.append(total_time)

for i in range(2,14):
    N = 2**i
    values.append(N)
    calc_time(N)

x = arange(len(values))
plot(x,dft_times,color='green')
plot(x,fft_times,color='blue')
show()
