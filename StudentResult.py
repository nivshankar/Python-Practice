class Student:
    __student_name=None
    __mark1=None
    __mark2=None
    __mark3=None
    avg=None
    def AvgDisplay(self,name,m1,m2,m3):
        if (m1<0 and m1>100) or (m2<0 and m2>100) or(m3<0 and m3>100):
            print("\nEnter marks of subjects in range 0 to 100")
        else:
            self.__student_name=name
            self.__mark1=m1
            self.__mark2=m2
            self.__mark3=m3
            self.avg=(m1+m2+m3)/3
            print("-"*70)
            print(f"Name of Student: {self.__student_name}")
            print(f"Mark1 :{self.__mark1}")
            print(f"Mark2 :{self.__mark2}")
            print(f"Mark3 :{self.__mark3}")
            print("\nAverage marks: %.2f"%(self.avg))
            print("-"*70)

    def Grade(self):
        if (self.__mark1>=34 and self.__mark1<=100) and (self.__mark2>=34 and self.__mark2<=100) and (self.__mark3>=34 and self.__mark3<=100):
            if self.avg>85:
                print(f"Grade of {self.__student_name} is A")
            elif self.avg>70:
                print(f"Grade of {self.__student_name} is B")
            elif self.avg>50:
                print(f"Grade of {self.__student_name} is C")
            elif self.avg>33:
                print(f"Grade of {self.__student_name} is D")
            else:
                print(f"Grade of {self.__student_name} is F(Fail)")
        else:
            print("Your Grade is not avaiable due to marks in one subject is less than 34")    
stud1=Student()
stud1.AvgDisplay('Neev',45,78,90)
stud1.Grade()
'''
Output:
----------------------------------------------------------------------
Name of Student: Neev
Mark1 :45
Mark2 :78
Mark3 :90

Average marks: 71.00
----------------------------------------------------------------------
Grade of Neev is B
'''