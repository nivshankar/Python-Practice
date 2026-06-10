class Student:
    RollNo=None
    def __init__(self,name,Mo_number,RNo):
        self.__name=name
        self.__Mobile=Mo_number
        self.__fee=40000
        self.RollNo=RNo
        self.__PaidFee = 0
        print("-"*90)
        print(f"Student name: {self.__name}")
        print(f"Student Mobile Number: {self.__Mobile}")
        print(f"Student Roll Number: {self.RollNo}")
        print("-"*90)
        self._remaining_fee=40000
    def Change_Name(self,name):
        self.__name=name
    def Change_Mobile_Student(self,MoNumber):
        self.__Mobile=MoNumber
    def Fee_Payment(self,amount):
        if amount<0 or amount>40000:
            print("Please enter valid amount to pay fee.")
        else:
            if (self.__PaidFee + amount)>self.__fee:
                print(f"The amount you added is more than you need to pay , you need to pay {self._remaining_fee}.")
            else:
                print(f"\n{amount} is paid to outstanding fee.")
                self.__PaidFee+=amount
                self._remaining_fee-=amount
                if self._remaining_fee!=0:
                    print(f"\nRemaining outstanding fee : {self._remaining_fee}\n")
                else:
                    print(f"\nYour {self.__fee} fees is  paid.")
stud1=Student('Neev Shankar',123456789,24)
stud1.Fee_Payment(10000)
stud1.Fee_Payment(17000)
stud1.Fee_Payment(10000)
stud1.Fee_Payment(5000)
stud1.Fee_Payment(3000)
"""
Output:
------------------------------------------------------------------------------------------
Student name: Neev Shankar
Student Mobile Number: 123456789
Student Roll Number: 24
------------------------------------------------------------------------------------------

10000 is paid to outstanding fee.

Remaining outstanding fee : 30000


17000 is paid to outstanding fee.

Remaining outstanding fee : 13000


10000 is paid to outstanding fee.

Remaining outstanding fee : 3000

The amount you added is more than you need to pay , you need to pay 3000.

3000 is paid to outstanding fee.

Your 40000 fees is  paid.
"""