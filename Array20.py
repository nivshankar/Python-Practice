size=int(input("\nEnter size of array : "))
print("\nEnter the elements of array: \n")
arr=[]
for i  in range(size):
    ele=int(input(f"arr[{i}] : "))
    arr.append(ele)
print(f"\n{arr[:5:]}")
print(f"\n{arr[::2]}")
'''
Output:

Enter size of array : 10

Enter the elements of array: 

arr[0] : 2
arr[1] : 5
arr[2] : 8
arr[3] : 9
arr[4] : 4
arr[5] : 43
arr[6] : 27
arr[7] : 38
arr[8] : 30
arr[9] : 69

[2, 5, 8, 9, 4]

[2, 8, 4, 27, 30]
'''