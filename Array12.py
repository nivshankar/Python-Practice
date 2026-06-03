size=int(input("\nEnter the size of Array 1: "))
print("\nEnter the elements for array 1: \n")
arr1=[]
for i in range(size):
    ele=int(input(f"arr1[{i}] : "))
    arr1.append(ele)
print(f"\nArray 1 : {arr1}")
size=int(input("\nEnter the size of Array 2: "))
print("\nEnter the elements for array 2: \n")
arr2=[]
for i in range(size):
    ele=int(input(f"arr2[{i}] : "))
    arr2.append(ele)
print(f"\nArray 2 : {arr2}")
new_array=[]
for i in arr1:
    new_array.append(i)
for i in arr2:
    new_array.append(i)
new_array.sort()
print(f"\nMerged array : {new_array}")
'''
Output:

Enter the size of Array 1: 3

Enter the elements for array 1: 

arr1[0] : 33
arr1[1] : 4
arr1[2] : 2

Array 1 : [33, 4, 2]

Enter the size of Array 2: 7

Enter the elements for array 2: 

arr2[0] : 80
arr2[1] : 6
arr2[2] : 5
arr2[3] : 99
arr2[4] : 54
arr2[5] : 65
arr2[6] : 22

Array 2 : [80, 6, 5, 99, 54, 65, 22]

Merged array : [2, 4, 5, 6, 22, 33, 54, 65, 80, 99]
'''