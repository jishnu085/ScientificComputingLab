x=int(input('enter the number '))
y=x
sum=0
n=0
while y>0:
    y//=10
    n=n+1

y=x

while y>0:
    d=y%10
    y=y//10
    sum=sum+d**n
if sum==x:
    print('armstrong')
else:
    print('not armstrong')