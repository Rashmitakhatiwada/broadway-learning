class Vehicle:
    def __init__(self):
        self.color='red'
        self._milage=99 #protected attributes

    def change_milage(self,milage):
        self._milage=milage

my_vehicle=Vehicle()
print(my_vehicle._milage)

my_vehicle.change_milage(25)
print(my_vehicle._milage)


"""this is also possible but not recomended"""

my_vehicle._milage=10
print(my_vehicle._milage)