class Account:
    __balance=0
    def deposit(self,amount):
        if amount<0:
            print("Please enter positive deposit amount.")
        else:
            self.__balance+=amount
            print(f"Amount Deposited: {amount}")
    def withdraw(self,amount):
        if amount<0:
            print("Please enter positive withdrawl amount.")
        elif amount>self.__balance:
            print("Insufficient Balance to withdraw given amount.")
        else:
            self.__balance-=amount
            print(f"Amount withdrawn: {amount}")
    def Display_balance(self):
        print(f"\nCurrent balance: {self.__balance}")

acc1=Account()
acc1.deposit(3000)
acc1.Display_balance()
acc1.withdraw(10000)
acc1.Display_balance()
acc1.deposit(3700)
acc1.Display_balance()
acc1.withdraw(4200)
acc1.Display_balance()
'''
Output:
Amount Deposited: 3000

Current balance: 3000
Insufficient Balance to withdraw given amount.

Current balance: 3000
Amount Deposited: 3700

Current balance: 6700
Amount withdrawn: 4200

Current balance: 2500
'''