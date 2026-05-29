def fact(n):
    if n<=1:
        return 1
    else:
        return n * fact(n-1)
n=int(input("Enter a number to getv it's factorial: "))
ans=fact(n)
print(f"Factorial of {n} is {ans}")
'''
Output:
nter a number to getv it's factorial: 7
Factorial of 7 is 5040
'''
