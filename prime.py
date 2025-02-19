n1=int(input('enter the first number = '))
n2=int(input('enter the second number= '))
x=[]

for i in range (n1,n2):
    count=0
    for j in range(1,n2):
        if (i%j==0):
            count=count+1
    if count==2:
        x.append(i)
 
print(x)
