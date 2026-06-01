#11 , 25 ==> 13,17,19,23
def Prime(n1,n2):
    if n1>n2:
        return Prime(n2,n1)
    if n1==2:
        print(n1)
    if n1<2:
        n1=2
        print(n1)
    else:
        i=2
        stop =False
        while i<n1:
            if n1%i==0:
                stop=True
                break
            i+=1
        if stop == False:
            print(n1)
    if n1!=n2:
        return Prime(n1 + 1,n2)

n1=int(input('Enter First Number: '))
n2=int(input('Enter Second Number: '))
Prime(n1,n2)
            
'''
Ouput:
Enter First Number: 12
Enter Second Number: 56
13
17
19
23
29
31
37
41
43
47
53
'''
            
