size=int(input("\nEnter the size of 1-D arrays: "))
print("\nEnter the elements for array 1: \n")
arr1=[]
for i in range(size):
    ele=int(input(f"arr1[{i}] : "))
    arr1.append(ele)
print("\nEnter the elements for array 2: \n")
arr2=[]
for i in range(size):
    ele=int(input(f"arr2[{i}] : "))
    arr2.append(ele)
addition_arr=[]    
for i in range(size):
    ele=arr1[i]+arr2[i]
    addition_arr.append(ele)   
print(f"\nThe new array of addition of two is : {addition_arr}") 
'''
Output:

Enter the size of 1-D arrays: 7

Enter the elements for array 1: 

arr1[0] : 1
arr1[1] : 2
arr1[2] : 3
arr1[3] : 56
arr1[4] : 4
arr1[5] : 7
arr1[6] : 44

Enter the elements for array 2: 

arr2[0] : 9
arr2[1] : 90
arr2[2] : 22
arr2[3] : 54
arr2[4] : 7
arr2[5] : 88
arr2[6] : 66

The new array of addition of two is : [10, 92, 25, 110, 11, 95, 110]
'''