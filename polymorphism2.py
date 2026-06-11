class shape:
    def area(self):
        return 0
class Circle(shape):
    def __init__(self,r):
        self.radius=r
    def area(self):
        return 3.14*self.radius**2
class Rectangle(shape):
    def __init__(self,l,b):
        self.length=l
        self.breadth=b
    def area(self):
        return self.breadth*self.length
arr=[Circle(9),Rectangle(10,12)]
for i in arr:
    print(f"Area of {i.__class__.__name__} is : {i.area()}")
'''
Output:
Area of Circle is : 254.34
Area of Rectangle is : 120
'''