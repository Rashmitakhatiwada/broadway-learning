class Vehicle:
    category = "car"


    @classmethod
    def printCategory(cls):
        print(f"Vehicle category = {cls.category}")


Vehicle.printCategory()

my_vehicle = Vehicle()
my_vehicle.printCategory()