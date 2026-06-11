class length_finding:
    def __init__(self,arg):
        self.datatype=arg
    def length(self):
        if type(self.datatype)==str:
            print(f"The length of string {self.datatype} is  : {len(self.datatype)}\n")
        elif type(self.datatype)==list:
            print(f"The length of list {self.datatype} is : {len(self.datatype)}\n")
        elif type(self.datatype)==dict:
            print(f"The length of dictionary {self.datatype} is : {len(self.datatype)}\n")
        else:
            print(f"The length function cannot be used for the following argument.\n")
objs=[length_finding('Hello World')
      ,length_finding([12,'Might','Universe',354,56.94,45,'Brian Lara'])
      ,length_finding({'abd':2,'egf':78,'Modi':'400 Paar','Midnight':'12 A.M'})
      ,length_finding(23)]
for i in objs:
    i.length()
'''
Output:
The length of string Hello World is  : 11

The length of list [12, 'Might', 'Universe', 354, 56.94, 45, 'Brian Lara'] is : 7

The length of dictionary {'abd': 2, 'egf': 78, 'Modi': '400 Paar', 'Midnight': '12 A.M'} is : 4

The length function cannot be used for the following argument.
'''