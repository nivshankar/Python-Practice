NoOfElements=int(input("\nEnter yhe number elements in each array: "))
print("\nEnter elements for array 1:\n")
arr1=[]
arr2=[]
for i in range(NoOfElements):
    element=int(input("arr1[{i}] : "))
    arr1.append(element)
print("\nEnter elements for array 2:\n")
for i in range(NoOfElements):
    element=int(input("arr2[{i}] : "))
    arr2.append(element)
for element in arr2:
    arr1.append(element)
print(f"\nThe two array are now one array as: \n{arr1}")
'''
Output:

Enter yhe number elements in each array: 5

Enter elements for array 1:

arr1[{i}] : 3
arr1[{i}] : 45
arr1[{i}] : 7
arr1[{i}] : 8
arr1[{i}] : 66

Enter elements for array 2:

arr2[{i}] : 99
arr2[{i}] : 5
arr2[{i}] : 6
arr2[{i}] : 77
arr2[{i}] : 5

The two array are now one array as: 
[3, 45, 7, 8, 66, 99, 5, 6, 77, 5]
'''