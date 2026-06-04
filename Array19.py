arr=[11,23,37,4,5,36,7,48,9,100,29]
num=int(input("\nEnter a number: "))
if num in arr:
    print(f"\nIndex of {num} is {arr.index(num)}")
else:
    print("\nNot found.")
'''
Output:
Case 1)

Enter a number: 34

Not found.

Case2)

Enter a number: 23

Index of 23 is 1
'''