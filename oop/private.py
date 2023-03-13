class Vehicle:
    def __init__(self):
        self.__color='red'


my_vehicle=Vehicle()
#can't access private members in thus way
print(my_vehicle.__color)

#can access protected member in this way but not recommended
print(my_vehicle._color)

#this is the name mangling . can access even private menbers
print(my_vehicle._vehicle__color)