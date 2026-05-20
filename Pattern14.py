for i in range(1,6):
    k=i
    for j in range(5,i-1,-1):
        print(k,end=" ")
        k+=1
    print()
'''
Output:
5 
4 5 
3 4 5 
2 3 4 5 
1 2 3 4 5 
'''
