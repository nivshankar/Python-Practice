size=int(input("\nEnter the size of array: "))
arr=[]
print("\nEnter the elements of array: \n")
for i in range(size):
    element=int(input(f"arr[{i}] : "))
    arr.append(element)
print(f"\nThe size of array is: {size}")
'''
Output:

Enter the size of array: 6

Enter the elements of array: 

arr[0] : 1
arr[1] : 2
arr[2] : 3
arr[3] : 5
arr[4] : 66
arr[5] : 7

The size of array is: 6
'''