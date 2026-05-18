n = int ( input ("Enter a number: "))
Sum=0
a=1
while a<=n:
    if a%2==0:
        Sum=Sum+a
    a+=1
print("The sum of even numbers from 1 to n is: ",Sum)

'''
Output:
Enter a number: 10
The sum of even numbers from 1 to n is:  30
'''
