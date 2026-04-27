## single level inheritance
class company:
    title: str = 'service_base'

    def __init__(self, name,rev):
        self.name = name
        self.rev = rev

    def info(self):
        print(f"company_name: {self.name}")

    def revenue_catg(self):
        if self.rev <= 5000:
            return "small"
        if self.rev > 100000:
            return "medium"
        else:
            print("lg")

class emp(company):

    def __init__(self, name, estd: int,rev:int):
        super().__init__(name,rev)   # call parent constructor
        self.estd = estd

    def final(self):
        print(f"company is established under named {self.name} and {self.estd}")


obj1 = emp("TCS", 1977,19000)
a= obj1.final()
print(obj1.revenue_catg())


## MULTIPLE LEVEL INHERITANCE

class p:

    def __init__(self,name,age):
        self.name = name 
        self.age = age

    def calx(self):
        return self.age * 365
    

class  c(p):

        def __init__(self,b_time,b_place,name,age):
            super().__init__(name,age)
            self.b_time = b_time
            self.b_place = b_place

        def info(self):
            print(f"chiled was born on {self.b_time} and {self.b_place} and age is {self.age}")

    
class gc(c):
        
        def __init__(self,gen,nat,b_time,b_place,name,age):
            super().__init__(b_time, b_place, name, age)
            self.gen = gen
            self.nat = nat
        
        def named(self):
            return (f"he is {self.gen} and he is mixed breed{self.nat} and his father place is {self.b_place}grand father age is {self.age}")
            


ob1 = c(706, 'kyd', 'siva', 1)
ob1.info()                 # no need to store (it prints directly)
print(ob1.calx())

obj2 = gc('genz', 'mexicanindo', '7:06', 'rajy', 'tata', 75)
print(obj2.named())
print(obj2.calx())


