class Vehicle:
    def __init__(self, color,doors):
        self.color=color #instances attributes
        self.doors=doors

class Bike(Vehicle):
    def __init__(self, color,doors,wheels):
        self.wheels=wheels
        super().__init__(doors,color)

class Car(Vehicle):
    def __init__(self, color,doors,milage):
        self.milage=milage
        super().__init__(doors,color)


honda=Bike('0','red',2)
rover= Car('white', '4',25)

print(rover.color)
print(honda.color)
print(honda.wheels)