import random
N=int(input('enter the number'))
r=[]
for i in range(0,N):
    toss=random.randint(0,1)
    if (toss)==0:
        r.append(1)
    else:
        r.append(0)
ph=(r.count(1)/N)
pt=(1-ph)
print('probability of heads = ',ph)
print('probability of tails= ',pt)