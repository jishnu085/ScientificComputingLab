from numpy import *
n=100000
sum=0
for i in range (0,1000000):
    fn=((-1)**i)/((2*i)+1)
    sum=sum+fn

sum1=sum*4    
error=abs(pi-sum1)
print('the sum is = ',sum1)
print('the error is = ',error)
