matrix=[]
print("\nEnter elements of a 2X3 matrix:\n")
for row in range(2):
    row_element=[]
    for col in range(3):
        ele=int(input(f'a[{row}][{col}] : '))
        row_element.append(ele)
    matrix.append(row_element)
print("\n","Transpose of the Matrix".center(100,"-"))
for i in range(3):
    print("\t\t\t\t\t\t",end="")
    for j in range(2):
        print(f"{matrix[j][i]}",end=" ")
    print()
'''
Output:

Enter elements of a 2X3 matrix:

a[0][0] : 1
a[0][1] : 4
a[0][2] : 6
a[1][0] : 7
a[1][1] : 3
a[1][2] : 5

 --------------------------------------Transpose of the Matrix---------------------------------------
                                                1 7 
                                                4 3 
                                                6 5 
'''