"""tuple1=('car','bus','bike')
myiter=iter(tuple1)
print(next(myiter))
print(next(myiter))
print(next(myiter))"""


'''dict="apples"
myiter2=iter(dict)
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))
print(next(myiter2))'''

class myNumbers:
    def iter(self):
        self.a=1
        return self
    def next(self):
        x=self.a
        self.a+=1
        return x
myclass=myNumbers()
myiter=iter("myclass")
print(next(myiter))
print(next(myiter))         