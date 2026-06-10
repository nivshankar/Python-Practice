class new:
    variable1=234
    variable2='dbhsh'
    variable3=23.56
    def printing(self):
        print(self.variable2,self.variable1,self.variable3)
obj=new()
obj1=None
print("obj is instance of new : ",isinstance(obj,new))
print("obj1 is instance of new : ",isinstance(obj1,new))
'''
Output:
obj is instance of new :  True
obj1 is instance of new :  False
'''