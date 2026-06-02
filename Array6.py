array=[8,46,98,300,3,23,7]
print(f"\nThe following is the array : \n{array}")
search_element=int(input("\nEnter element to search in the array: "))
if search_element in array:
    print(f"It's index no in the array  is : {array.index(search_element)}")
else:
    print("\nThe element not found in the  array")
'''
Output:
Case1:

The following is the array : 
[8, 46, 98, 300, 3, 23, 7]

Enter element to search in the array: 7
It's index no in the array  is : 6

Caes 2)

The following is the array : 
[8, 46, 98, 300, 3, 23, 7]

Enter element to search in the array: 1

The element not found in the  array
'''