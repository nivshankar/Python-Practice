class new:
    variable1=234
    variable2='dbhsh'
    variable3=23.56
    def printing(self):
        print(self.variable2,self.variable1,self.variable3)
print("The following is the list of attributes and methods:")
for properties in dir(new):
    print(properties)
'''
Output:
The following is the list of attributes and methods:
__class__
__delattr__
__dict__
__dir__
__doc__
__eq__
__firstlineno__
__format__
__ge__
__getattribute__
__getstate__
__gt__
__hash__
__init__
__init_subclass__
__le__
__lt__
__module__
__ne__
__new__
__reduce__
__reduce_ex__
__repr__
__setattr__
__sizeof__
__static_attributes__
__str__
__subclasshook__
__weakref__
printing
variable1
variable2
variable3
'''