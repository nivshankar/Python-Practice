#anything
#gnihtyna
def RevString (string):
    length=len(string)
    if length == 1:
        return string
    else:
        return RevString(string[1::])+string[0]

string=input('Enter a string to reverse it : ')
reverse=RevString(string)
print(f"The reverse of string '{string}' is '{reverse}'")
'''
Output:
case 1)
Enter a string to reverse it : Demonstration
The reverse of string 'Demonstration' is 'noitartsnomeD'
case 2)
Enter a string to reverse it : a
The reverse of string 'a' is 'a'
case 3)
Enter a string to reverse it : a
The reverse of string 'a' is 'a'
'''
