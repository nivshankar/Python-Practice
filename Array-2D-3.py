row_size=int(input('\nEnter row size of matrix: '))
col_size=int(input('\nEnter column size of matrix: '))
matrix=[]
sum=0
print("\n","Enter array elements".center(100,"-"))
for row in range(row_size):
    row_element=[]
    for col in range(col_size):
        ele=int(input(f'a[{row}][{col}] : '))
        row_element.append(ele)
        sum+=ele
    matrix.append(row_element)    
print(f"\nThe sum of all elements is: {sum}")
'''
Output:

Enter row size of matrix: 3

Enter column size of matrix: 3

 ----------------------------------------Enter array elements----------------------------------------
a[0][0] : 1
a[0][1] : 2
a[0][2] : 3
a[1][0] : 5
a[1][1] : 7
a[1][2] : 88
a[2][0] : 5
a[2][1] : 6
a[2][2] : 34

The sum of all elements is: 151
'''