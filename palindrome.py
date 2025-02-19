def palindrome(n):
    
    num_str = str(n)
    
    return num_str == num_str[::-1]


n = int(input("Enter a number to check if it's a palindrome: "))

if palindrome(n):
    print(n, "is a palindrome number.")
else:
    print(n, "is not a palindrome number.")
