class Book:
    _title=None
    _author=None
    def setter(self,title,author):
        self._author=author
        self._title=title
    def getter(self):
        print(f"\nAuthor: {self._author}\nTitle: {self._title}")

b1=Book()
b1.setter('Pride and Prejudice','Jane Austen') 
b1.getter() 

b2=Book()
b2.setter('Crime and Punishment','Fyodor Dostoevsky') 
b2.getter()

b3=Book()
b3.setter(1984,'George Orwell') 
b3.getter()
"""
Output:

Author: Jane Austen
Title: Pride and Prejudice

Author: Fyodor Dostoevsky
Title: Crime and Punishment

Author: George Orwell
Title: 1984
"""