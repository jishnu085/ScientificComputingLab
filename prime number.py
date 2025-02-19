def prime(a):
    p=0
    for i in range(2,a):
        if a%i==0:
            p+=1
             
    if p==0:
        return True
for a in range(2,100):
    if prime(a):
        print(a)


    
    


 
        


           
