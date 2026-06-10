class Animal:
   def __init__(self, name):
       self.name = name
class Dog(Animal):
   def speak(self):
       print(f"{self.name} says Bhow Bhow!")
class Cat(Animal):
   def speak(self):
       print(f"{self.name} says Meow !")
# Usage
dog = Dog("Raju")
cat = Cat("Divyesh Jadu")
dog.speak()
cat.speak()
'''
Output:
Raju says Bhow Bhow!
Divyesh Jadu says Meow !
'''