class Transport:
    def travel(self):
        pass
class Train(Transport):
    def travel(self):
        print('Train travels on railway tracks')
class Plane(Transport):
    def travel(self):
        print('Plain  travels in sky,faster than trains')
objs=[Train(),Plane()]
for i in objs:
    i.travel()
'''
Output:
Train travels on railway tracks
Plain  travels in sky,faster than trains
'''
