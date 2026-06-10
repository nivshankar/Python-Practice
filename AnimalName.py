class Animal:
    _name=None
    def __init__(self):
        self._name='Cat'
    def Display(self):
        print(f"\nName of the Animal is : {self._name}\n")
animal=Animal()
animal.Display()
'''
Output:

Name of the Animal is : Cat

'''