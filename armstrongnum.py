# def is_armstrong(n):

#   if n <= 0:
#     return False

  
#   num_digits = len(str(n))

  
#   sum_of_digits = 0

#   temp = n
#   while temp > 0:
#     digit = temp % 10
#     sum_of_digits += digit ** num_digits
#     temp //= 10

  
#   return sum_of_digits == n


# num = int(input("Enter a number: "))





# if is_armstrong(num):
#   print(num, "is an Armstrong number!")
# else:
#   print(num, "is not an Armstrong number.")

























# def armstrong(n):
#     if n<=0:
#         return False
#     no_of_digits = len(str(n))
#     temp = n
#     sum_of_digits=0
#     while temp>0:
#         digit = temp%10
#         sum_of_digits = sum_of_digits + digit**no_of_digits
#         temp = temp//10
#     return sum_of_digits==n

# n=int(input("enter a number"))

# if armstrong(n):
#     print(n,"is a armstrong number ")
# else:
#     print(n ,"is not a armstrong number")









def armstrong(n):
    if n<=0:
        return False

    nod=len(str(n))
    sod=0
    temp=n
    while temp>0:
        digit=temp%10
        sod=sod+digit**nod
        temp=temp//10
    return sod==n

n=int(input("ENTER A NUMBER = "))
if armstrong(n):
    print(n,"is  ARMSTRONG")
else:
    print(n,"is NOT ARMSTRONG")

