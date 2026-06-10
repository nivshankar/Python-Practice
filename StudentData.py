class Student:
    RollNo=None
    def __int__(self,name,Mo_number,RNo):
        self.__name=name
        self.__Mobile=Mo_number
        self.__fee=40000
        self.RollNo=RNo
    def Change_Name(self,name):
        self.__name=name
    def Change_Mobile_Student(self,MoNumber):
        self.__Mobile=MoNumber
    def Fee_Payment(self,)