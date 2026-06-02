arr=[]
NumOfElement=int(input("Enter the number of elements of array: "))
sum=0
for i in range(NumOfElement):
    element=int(input(f"Enter element arr[{i}]7:  "))
    arr.append(element)
    sum+=element
print(f"The sum of elements of array is: {sum}")
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