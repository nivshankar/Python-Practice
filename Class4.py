class Calculation:
    '''
    This class is based on various mathematical caluculations like
    Addition ,subtraction,multiplication.
    '''
    def addition(self,a,b):
        '''
        This method of class helps to calculate the sum of two number
        given as argument.

        Both numbers are integer.

        If decimal number added as argument it will be automatically 
        converted to integers.
        '''
        return self.a+self.b
    
    def substraction(self,a,b):
        '''
        This method of class helps to calculate the substraction of two 
        numbers given as argument.

        Both numbers are integer.

        If decimal number added as argument it will be automatically 
        converted to integers.

        first argument is substracted by the  second one
        '''
        return self.a+self.b
obj=Calculation()
help(Calculation)
'''
Output:
Help on class Calculation in module __main__:                                                                    

class Calculation(builtins.object)
 |  This class is based on various mathematical caluculations like
 |  Addition ,subtraction,multiplication.
 |
 |  Methods defined here:
 |
 |  addition(self, a, b)
 |      This method of class helps to calculate the sum of two number
 |      given as argument.
 |
 |      Both numbers are integer.
 |
 |      If decimal number added as argument it will be automatically
 |      converted to integers.
 |
 |  substraction(self, a, b)
 |      This method of class helps to calculate the substraction of two
 |      numbers given as argument.
 |
 |      Both numbers are integer.
 |
 |      If decimal number added as argument it will be automatically
 |      converted to integers.
 |
 |      first argument is substracted by the  second one
 |
 |  ----------------------------------------------------------------------
 |  Data descriptors defined here:
 |                                                                                                               
 |  __dict__
 |      dictionary for instance variables
 |
 |  __weakref__
 |      list of weak references to the object 
'''