class Teacher:
    def __init__(self):
        self._teacher_name='Mayur Modi'
        self._salary=70000
class Administrator:
    def Student_data(self):
        self._student_name='Neev Shankar'
        self._course='Computer Engineering'
class Headmaster(Teacher,Administrator):
    def Display(self):
        print(f"\nTeacher: {self._teacher_name}\nSalary: {self._salary}")
        print(f"\nStudent: {self._student_name}\nCourse: {self._course}")
obj=Headmaster()
obj.Student_data()
obj.Display()
'''
Output:

Teacher: Mayur Modi
Salary: 70000

Student: Neev Shankar
Course: Computer Engineering
'''