class car:

    def __init__(self,price,owner_address):
        self.price = price #public
        self.__owner_address = owner_address # private
    
    def fx1(self):
        print(f"this car is owned and parked at {self.__owner_address}")

    def fx2(self):
        print(f"the price of the car is {self.price}")

obj1 = car(7600,'Tampa_61')
#obj1._car__owner_address = 'panama_661'
obj1.fx1()


