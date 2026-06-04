size=int(input("\nEnter the size of array: "))
arr=[]
print("\nEnter the elements of array: \n")
sum=0
for i in range(size):
    element=int(input(f"arr[{i}] : "))
    arr.append(element)
    sum+=element
avg=sum/size
print("\nThe average of the elements of array is : %.2f"%(avg))
'''
Output:

Enter the size of array: 7

Enter the elements of array: 

arr[0] : 4
arr[1] : 6
arr[2] : 8
arr[3] : 45
arr[4] : 6
arr[5] : 43
arr[6] : 77

The average of the elements of array is : 27.0
'''