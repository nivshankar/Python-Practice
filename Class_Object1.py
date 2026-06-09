class Person:
    name=None
    age=None
    def Display(self):
        print("*"*40,f"\n\nName: {self.name}\nAge: {self.age}\n\n","*"*40)

p2=Person()
p2.name="Neev"
p2.age=19
p2.Display()
p3=Person()
p3.name='Aryan'
p3.age=19
p3.Display()
p=Person()
p.name='Karm'
p.age=10
p.Display()
'''
Output:
**************************************** 

Name: Neev
Age: 19

 ****************************************
**************************************** 

Name: Aryan
Age: 19

 ****************************************
**************************************** 

Name: Karm
Age: 10

 ****************************************
'''