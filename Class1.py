class Main:
    variable='Hello'
    variable1=456
    def method(self):
        print("The method of the class")
obj=Main()
print(type(obj.method))
print(type(obj.variable))
print(type(obj.variable1))
print(type(obj))
'''
Output:
<class 'method'>
<class 'str'>
<class 'int'>
<class '__main__.Main'>
'''