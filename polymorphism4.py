class calculator:
    def multiply(self,*args):
        if len(args)==0:
            print("Give atleast 2 arguments to multiply them.")
        elif len(args)==1:
            print("Give atleast 2 arguments to multiply them.")
        else:
            ans=1
            for i in args:
                ans*=i
            print(f"The multiplication of ",end="")
            for i in args:
                print(i,end=",")
            print(f" is {ans}")
num=int(input('\nEnter the number of time you want ot run calculator: '))
objs=[]
for _ in range(num):
    objs.append(calculator())
#arguments 
for i,calc in enumerate(objs,1):
    print(f"\n-----Calculator {i}-----")
    no_of_arg=int(input('\nEnter how many numbers you want to multiply: '))
    numbers=[]
    for _ in range (no_of_arg):
        num=int(input('Enter number : '))
        numbers.append(num)
    multiplication=calc.multiply(*numbers)
'''
Output:    

Enter the number of time you want ot run calculator: 5

-----Calculator 1-----

Enter how many numbers you want to multiply: 3
Enter number : 2
Enter number : 5
Enter number : 6
The multiplication of 2,5,6, is 60

-----Calculator 2-----

Enter how many numbers you want to multiply: 2
Enter number : 2
Enter number : 89
The multiplication of 2,89, is 178

-----Calculator 3-----

Enter how many numbers you want to multiply: 6
Enter number : 5
Enter number : 8
Enter number : 9
Enter number : 10
Enter number : 4
Enter number : 1
The multiplication of 5,8,9,10,4,1, is 14400

-----Calculator 4-----

Enter how many numbers you want to multiply: 3
Enter number : 10
Enter number : 23
Enter number : 4
The multiplication of 10,23,4, is 920

-----Calculator 5-----

Enter how many numbers you want to multiply: 4
Enter number : 37
Enter number : 33
Enter number : 3
Enter number : 3
The multiplication of 37,33,3,3, is 10989   
'''