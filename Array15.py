def prime_numbers (n1,n2,prime_list=[]):
    if n1==n2:
        return prime_list
    if n2>n1:
        if n1>=2:
            prime=True
            for i in range(2,n1):
                if n1%i==0:
                    prime=False
                    break
            if prime:
                prime_list.append(n1)
            return prime_numbers (n1+1,n2,prime_list)
        else:
            n1=2
            return prime_numbers (n1,n2,prime_list=[])
    else:
        return prime_numbers (n2,n1,prime_list)
while True:
    n1=int(input("\nEnter first number: "))
    n2=int(input("Enter second number: "))
    if n1==n2:
        print("\nPlease enter two different numbers.")
        continue
    if n1<0 and n2<0:
        print("\nPlease enter at least 1 positive number.")
        continue
    else:
        prime_list=prime_numbers (n1,n2)
        print("\n","These are the following prime numbers in given range:".center(90,"-"))
        for i in prime_list:
            print(f"{i}".center(50))
        break
'''
Output:

Enter first number: 3
Enter second number: 3

Please enter two different numbers.

Enter first number: -4
Enter second number: -4

Please enter two different numbers.

Enter first number: -7
Enter second number: -56

Please enter at least 1 positive number.

Enter first number: -5
Enter second number: 45 

 ------------------These are the following prime numbers in given range:-------------------
                        2                         
                        3                         
                        5                         
                        7                         
                        11                        
                        13                        
                        17                        
                        19                        
                        23                        
                        29                        
                        31                        
                        37                        
                        41                        
                        43 
'''
    