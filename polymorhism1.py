class Addition:
    def add(self,*args):
        if not args:
            print("\nGive two arguments.\n")
        elif len(args)==1:
            print("\nGive two arguments.\n")
        elif len(args)==2:
            print(f"\nAddition: {args[0]+args[1]}\n")
        else:
            print("\nGive two arguments only.\n")

obj=Addition()
obj.add()
obj.add(100)
obj.add(12,24)
obj.add('Hello ','World')
'''
Output:

Give two arguments.


Give two arguments.


Addition: 36


Addition: Hello World

'''