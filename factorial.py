# # from numpy import *
# # def factorial(n):
# #     if n == 0:
# #         return 1
# #     else:
# #         return n * factorial(n - 1)

# # # Taking input from the user
# # num = int(input("Enter a number: "))

# # # Checking if the number is negative
# # if num < 0:
# #     print("Factorial does not exist for negative numbers.")
# # elif num == 0:
# #     print("The factorial of 0 is 1")
# # else:
# #     print("The factorial of", num, "is", factorial(num))

# from numpy import *
# def fat(n):
#     if n==0:
#         return 1
#     else:
#         return n * fat(n-1)


# k=fat(5)
# print(k)
# 1
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)
    
num=int(input('enter a number = '))
print(factorial(num))
