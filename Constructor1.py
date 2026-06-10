class Rectangle:
    _length=None
    _width=None
    def __init__(self,l,w):
        self._length=l
        self._width=w
        print(f"\nThe Area of the Rectangle is: {self._width * self._length}")
Rect=Rectangle(int(input('Enter length : ')),int(input('Enter width : ')))
'''
Output:
Enter length : 10
Enter width : 23

The Area of the Rectangle is: 230
'''
