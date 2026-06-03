size=int(input("\nEnter the size of array: "))
arr=[]
print("\nEnter the elements of array: \n")
sum=0
for i in range(size):
    element=int(input(f"arr[{i}] : "))
    arr.append(element)
    sum+=element
print(f"\nThe following is the array you entered:\n{arr}")
print(f"\nThe sum of all elements of array is : {sum}")
'''
Output:

Enter the size of array: 7

Enter the elements of array: 

arr[0] : 34
arr[1] : 5
arr[2] : 88
arr[3] : 6
arr[4] : 3
arr[5] : 66 
arr[6] : 89

The following is the array you entered:
[34, 5, 88, 6, 3, 66, 89]

The sum of all elements of array is : 291
'''