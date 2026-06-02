array=[78,76,498,300,3,23,1,77]
print(f"\nThe following is the present array : \n{array}")
delete=int(input("\nEnter the element to delete: "))
if delete in array:
    array.remove(delete)
    print(f"\nThe updated element is : \n{array}")
else:
    print("\nThe element entered is not present in the array.")
'''
Output:
Case 1)
The following is the present array : 
[78, 76, 498, 300, 3, 23, 1, 77]

Enter the element to delete: 2

The element entered is not present in the array.

Case 2)

The following is the present array : 
[78, 76, 498, 300, 3, 23, 1, 77]

Enter the element to delete: 76

The updated element is : 
[78, 498, 300, 3, 23, 1, 77]
'''