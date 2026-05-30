#0 1 1 2 3 5 8
def Fibonacci(n):
   if n<0 :
       print("Please enter a numer greater than or equal to 0")
       return 0
    if n<=1:
        return n
    if n>=3:
        return Fibonacci(n-1)+Fibonacci(n-2)
n=int(input("Enter a serial number to find Fibonacci number \nAt that serial number in the series: "))
ans=Fibonacci(n)
print(f"The number at {n} serial number in Fibonacci Series is : {ans}")
