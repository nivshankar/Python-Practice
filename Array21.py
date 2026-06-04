size=int(input("\nEnter size of array : "))
print("\nEnter the elements of array: \n")
arr=[]
for i  in range(size):
    ele=int(input(f"arr[{i}] : "))
    arr.append(ele)
print(f"\nFirst element: {arr[0]}")
print(f"\nMiddle element: {arr[int(size/2)]}")
print(f"\nFirst element: {arr[size-1]}")
'''
Output:

Enter size of array : 7

Enter the elements of array: 

arr[0] : 1
arr[1] : 2
arr[2] : 3
arr[3] : 4
arr[4] : 5
arr[5] : 6
arr[6] : 7

First element: 1

Middle element: 4

First element: 7
'''