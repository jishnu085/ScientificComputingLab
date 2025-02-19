def palindrome(n):
    
    j=n[::-1]
    return n==j


n=(input('enter a number'))

if palindrome(n):
    print(n,"is palindrome")
else:
    print(n,"is not palindrome")
    