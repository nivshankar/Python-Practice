n=int(input("Enter any number :"))
if n<15:
    print("There is no number from 0 to n divisible by both 3 and 5")
else: 
    a=15
    while a<=n:
        if a%15==0:
            print(a ,end=" ")
        a+=1
        
'''
Output:
Enter any number :45
15 30 45 
'''
