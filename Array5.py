array=[8,46,98,300,3,23,7]
print(f"\nThe following is the present array : \n{array}")
find_index=int(input("Enter index number to update element: "))
if find_index > (len(array)-1) and find_index < 0: 
    print("\nPlese give valid valid index number.")
else:
    while True:
        print("\nThe follwing updation is available:\n1)Update Element\n2)Delete Element")
        update_choice=int(input("Enter your choice : "))
        match  update_choice:
            case 1:
                update_element=int(input("\nGive the new element"))
                array.insert(find_index,update_element)
                print(f"\nThe following is the updated array : \n{array}")
                break
            case 2:
                array.pop(find_index)
                print(f"\nThe following is the updated array : \n{array}")
                break
            case _:
                print("\nPlease enter valid option number")
'''
Output:

The following is the present array : 
[8, 46, 98, 300, 3, 23, 7]
Enter index number to update element: 1

The follwing updation is available:
1)Update Element
2)Delete Element
Enter your choice : 9

Please enter valid option number

The follwing updation is available:
1)Update Element
2)Delete Element
Enter your choice : 1

Give the new element34

The following is the updated array : 
[8, 34, 46, 98, 300, 3, 23, 7]
'''