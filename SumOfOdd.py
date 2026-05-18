n = int ( input ("Enter a number: "))
Sum=0
a=1
while a<=n:
    if a%2!=0:
        Sum=Sum+a
    a+=1
print("The sum of odd numbers from 1 to n is: ",Sum)

'''
Output:
Enter a number: 9
The sum of odd numbers from 1 to n is:  25
'''
