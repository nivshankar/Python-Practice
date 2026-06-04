matrix=[]
print("\nEnter elements of 3X3 matrix: \n")
for row in range(3):
    Row_element=[]
    for col in range(3):
        ele=int(input(f"a[{row}][{col}] : "))
        Row_element.append(ele)
    matrix.append(Row_element)
print("\n","The matrix in tabular form ".center(90,"-"))
for row in matrix:
    for ele in row:
        print(ele,end="  ")
    print("\n")
'''
Output:

Enter elements of 3X3 matrix: 

a[0][0] : 3
a[0][1] : 4
a[0][2] : 8
a[1][0] : 9
a[1][1] : -3
a[1][2] : -5
a[2][0] : -9
a[2][1] : 20
a[2][2] : 2

 -------------------------------The matrix in tabular form --------------------------------
3  4  8  

9  -3  -5  

-9  20  2 
'''