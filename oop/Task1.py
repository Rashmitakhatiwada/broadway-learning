class Dog:
    def __init__(self,color,legs):
        self.color=color
        self.legs=legs

    def make_it_white(self):
        self.color= "white"

dog1 = Dog('brown','4')

print(f"this dog is {dog1.color} and has {dog1.legs} legs")
dog1.make_it_white()
print(f"new color is {dog1.color}")