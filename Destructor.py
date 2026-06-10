class Observe:
    object=None
    def __init__(self,object):
        self.object=object
    def __del__(self):
        print(f"The destructor is used for {self.object}")
obj1=Observe('obj1')
obj2=Observe('obj2')
del obj2
'''
Output:
The destructor is used for obj2
The destructor is used for obj1
'''