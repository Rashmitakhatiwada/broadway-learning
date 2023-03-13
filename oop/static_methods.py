#static methods is used when we do not want our method to call cls or self.
class Vehicle:
    @staticmethod
    def is_good_mileage(mileage):
        if mileage < 25:
            return "No"
        return "Yes"

print(Vehicle.is_good_mileage(25))
print(Vehicle.is_good_mileage(5))