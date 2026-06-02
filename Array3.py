array=[2,56,46,79,80,456]
print(f"The following is the present array : \n{array}")
NewElement=int(input("\nEnter the new element: "))
index=int(input("Enter Position to insert the element in array  : "))
if index>len(array) and index<1:
    print("Please enter valid postion to insert the element in array.")
else:
    array.insert(index-1,NewElement)
print(f"\nThe updated element is : \n{array}")
'''
Output:
Enter the number of elements of array: 7
Enter element arr[0]:  1
Enter element arr[1]:  2
Enter element arr[2]:  3
Enter element arr[3]:  55
Enter element arr[4]:  3
Enter element arr[5]:  6 
Enter element arr[6]:  8
The sum of elements of array is: 78
'''