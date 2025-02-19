from numpy import *
fibonacci=[0,1]
def fibo(n):
    while len(fibonacci)<n:
        s=fibonacci[-1]+fibonacci[-2]
        fibonacci.append(s)
fibo(100)
print(fibonacci)