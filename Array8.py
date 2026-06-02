size=int(input("\nEnter the size of array: "))
arr=[]
print("\nEnter the elements of array: \n")
for i in range(size):
    element=int(input(f"arr[{i}] : "))
    arr.append(element)
once=True
for_once=True
for i in arr:
    if i%2==0:
        if once==True:
            once=False
            print("\nEven numbers in array are: ",end="")
        print(i,end=', ')
for i in arr:
    if i%2!=0:
        if for_once==True:
            for_once=False
            print("\nOdd numbers in array are: ",end="")
        print(i,end=', ')
'''
Output:

Enter the size of array: 10

Enter the elements of array: 

arr[0] : 12
arr[1] : 35
arr[2] : 3467
arr[3] : 59
arr[4] : 56
arr[5] : 98
arr[6] : 86
arr[7] : 576
arr[8] : 495
arr[9] : 2990

Even numbers in array are: 12, 56, 98, 86, 576, 2990, 
Odd numbers in array are: 35, 3467, 59, 495, 
'''