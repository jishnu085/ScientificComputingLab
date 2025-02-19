import random
def cointoss(num):
    recordList=[]
    for i in range(num):
        flip=random.randint(0,1)
        if flip==0:
            recordList.append(0)
        else:
            recordList.append(1)
    print(recordList)
    print("no Of Heads = ",recordList.count(1))


cointoss(10)


