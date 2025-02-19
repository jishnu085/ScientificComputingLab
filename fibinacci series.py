#from numpy import *
#def fib(n):
   # fibseries=[0,1]
   # while len(fibseries)<n:
     #   fibseries.append(fibseries[-1]+fibseries[-2])
   # return fibseries
#n=10
#s=fib(n)  
#print(s)





def finonacci(n):
    fibseries=[0,1]
    while len(fibseries)<n:
        fibseries.append(fibseries[-1]+fibseries[-2])
    return fibseries
n=100
s=finonacci(n)
print(s)    