class AgeValidator:
    __age=0
    def setter(self,age):
            self.__age=age
    def getter(self):
        if self.__age<0:
            print(f"\n{self.__age} is not Valid age.")
        else:
            print(f"\n{self.__age} is valid age.")
Year=AgeValidator()
Year.setter(10)
Year.getter()

Year1=AgeValidator()
Year1.setter(-16)
Year1.getter()
'''
Output:

10 is valid age.

-16 is not Valid age.
'''