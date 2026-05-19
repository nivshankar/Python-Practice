for i in range(1,6):
    for _ in range(5,i,-1):
        print(" ",end =" ")
    for j in range(1,i+1):
        print(i,end=" ")
    print()
'''
Output:
        1 
      2 2 
    3 3 3 
  4 4 4 4 
5 5 5 5 5
'''
