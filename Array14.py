size=int(input("\nEnter Array size: "))
print("\n Enter Array's elements :\n")
def fact(n):
    if n<=1:
        return 1
    else:
        return n*fact(n-1)
arr=[]
for i in range(size):
    ele=int(input(f"arr[{i}] : "))
    arr.append(ele)
print("\nThe factorial of elements of array are: \n")
for i in arr:
    print(fact(i),end=", ")
'''
Output:

Enter Array size: 6

 Enter Array's elements :

arr[0] : 3
arr[1] : 7
arr[2] : 6
arr[3] : 5
arr[4] : 9
arr[5] : 10

The factorial of elements of array are: 

6, 5040, 720, 120, 362880, 3628800, 
'''