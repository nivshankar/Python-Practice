class Employee:
    def __init__(self):
        self.__salary=100000
        self.__role='Senior Engineer'
        self.__HrsOfWork=8
    def __del__(self):
        print("\nEmployee Resign permit ==> Successful.\n")
        print("Thank you for working with us,we appreciate all the efforts you put on.")
emp1=Employee()
del emp1
'''
Output:

Employee Resign permit ==> Successful.

Thank you for working with us,we appreciate all the efforts you put on.
'''