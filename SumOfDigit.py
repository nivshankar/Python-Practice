#2732 ==> 2+7+3+2 =14
def SumOfDigit(n):
    if n<10:
        return n
    else:
        return (n%10)+SumOfDigit(int(n/10))

num= int(input("\n\t\tEnter a number : "))
ans=SumOfDigit(num)
print(f"\n\t\tAnswer of Digits in the number is : {ans}")

'''
Output:

		Enter a number : 12345

		Answer of Digits in the number is : 15
'''
