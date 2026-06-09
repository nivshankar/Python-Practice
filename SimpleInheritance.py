class Parent:
    def display(self):
        print('-'*70)
        print("This is the display method of parent class.")
        print('-'*70)
class Child(Parent):
    pass
obj=Child()
obj.display()
'''
Output:
----------------------------------------------------------------------
This is the display method of parent class.
----------------------------------------------------------------------
'''