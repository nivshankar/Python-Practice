size=int(input("\nEnter the size of array: "))
arr=[]
print("\nEnter the elements of array: \n")
for i in range(size):
    element=int(input(f"arr[{i}] : "))
    arr.append(element)
print("\nSquare of all elements of array are:\n")
for i in arr:
    print(i**2,end=' ')
'''
Output:

Enter the size of array: 7

Enter the elements of array: 

arr[0] : 1
arr[1] : 2
arr[2] : 3
arr[3] : 4
arr[4] : 6
arr[5] : 77
arr[6] : 5

Square of all elements of array are:

1 4 9 16 36 5929 25
'''