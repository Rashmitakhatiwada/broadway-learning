class Vehicle:
    category ='car' #class attributes
    def __init__(self, color,doors):
        self.color=color #instances attributes
        self.doors=doors

    def description(self):
        return f"this vechile color is {self.color} and it has {self.doors} doors."


    # def make_it_blue(self):
    #     self.color="blue"


rover= Vehicle('red', '4')
new_rover= Vehicle('white', '3')

# print(rover.description())
print(f"before {rover.color}")
rover.color="blue"
# rover.make_it_blue() #mathiko and this both gives a same result
print(f"after {rover.color}")
print(f"new vechile color {new_rover.color}")
print(f"new vechile doors {new_rover.doors}")
# print(f"vehicle color :{rover.color}")
# print(f"vehicle category :{rover.category}")
# print(f"numbers of doors :{rover.doors}")

# print(f"category:{rover.__class__.category}")