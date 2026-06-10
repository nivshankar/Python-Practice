class Student1:
    def __init__(self):
        self.stud1='Neev'
        self.id1=23
        self.age1=19
        self.rol1='Student'
        print('-'*75)
        print(f"Role: {self.rol1}\nName: {self.stud1}\nAge: {self.age1}\nId: {self.id1}")
        print('-'*75)
class Student2:
    def display_student2(self):
        self.stud2='Modi'
        self.id2=400
        self.age2=20
        self.rol2='Student'
        print('-'*75)
        print(f"Role: {self.rol2}\nName: {self.stud2}\nAge: {self.age2}\nId: {self.id2}")
        print('-'*75)
class Teacher(Student1,Student2):
    def __init__(self):
        super().__init__()
        self.t1='Mariel'
        self.id3=229
        self.age3=55
        self.rol3='Tecacher'
        print('-'*75)
        print(f"Role: {self.rol3}\nName: {self.t1}\nAge: {self.age3}\nId: {self.id3}")
        print('-'*75)
class Admin(Teacher):
    def __init__(self):
        super().__init__()
        self.ad1='Joe Biden'
        self.id4=231
        self.age4=65
        self.rol4='Admin'
        print('-'*75)
        print(f"Role: {self.rol4}\nName: {self.ad1}\nAge: {self.age4}\nId: {self.id4}")
        print('-'*75)
class Principal(Admin):
    def __init__(self):
        super().__init__()
        self.p1='John Snow'
        self.id5=235
        self.age5=25
        self.rol5='King of North'
        print('-'*75)
        print(f"Role: {self.rol5}\nName: {self.p1}\nAge: {self.age5}\nId: {self.id5}")
        print('-'*75)
obj=Principal()

obj.display_student2()
'''
Output:
---------------------------------------------------------------------------
Role: Student
Name: Neev
Age: 19
Id: 23
---------------------------------------------------------------------------
---------------------------------------------------------------------------
Role: Tecacher
Name: Mariel
Age: 55
Id: 229
---------------------------------------------------------------------------
---------------------------------------------------------------------------
Role: Admin
Name: Joe Biden
Age: 65
Id: 231
---------------------------------------------------------------------------
---------------------------------------------------------------------------
Role: King of North
Name: John Snow
Age: 25
Id: 235
---------------------------------------------------------------------------
---------------------------------------------------------------------------
Role: Student
Name: Modi
Age: 20
Id: 400
---------------------------------------------------------------------------
'''