class Counter:
    count=0
    def increment(self):
        self.count+=1
    def Display(self):
        print(f"Count = {self.count}")
c=Counter()
c.increment()
c.increment()
c.increment()
c.Display()
'''
Output:
Count = 3
'''