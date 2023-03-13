from datetime import date

class Person:
    def __init__(self , name , age):
        self.name = name
        self.age = age

    @classmethod
    def fromBirthYear(cls, name, year):
        return cls(name, date.today().year - year)


    def display(self):
        print(f"{self.name} is {self.age} years old")


john = Person("john", 21)
john.display()

# raj=Person("raj", 23)
ram= Person.fromBirthYear("raj", 2005)
ram.display()