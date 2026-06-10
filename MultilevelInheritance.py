class Grandparent:
    def Eldest(self):
        self.grandparent_name='Arthur Bennett'
        print(f"\nGrandparent: {self.grandparent_name}")
class Parent(Grandparent):
    def Father(self):
        self.parent_name='Charles Bennett'
        print(f"\nParent: {self.parent_name}")
class Child(Parent):
    def Son(self):
       self.child_name='David Bennett'
       print(f"\nChild: {self.child_name}")
Hierarchy1=Child()
Hierarchy1.Eldest()
Hierarchy1.Father()
Hierarchy1.Son()
'''
Output:

Grandparent: Arthur Bennett

Parent: Charles Bennett

Child: David Bennett
'''        