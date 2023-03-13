# #a class with same name but diffrent types of arguemnt displays an error
# class Shape:
#     def area(self, l):
#         return l * l
#
#     def area(self, l, b):
#         return l * b
#
# square = Shape()
# print(square.area(5)) #if same methods name it goes for the latest one

#problem solving
class Shape:
    def area(self, l, b= None):
        if b is not None:
            return l * b
        return l * l

square= Shape()
print(square.area(5))
print(square.area(5,4))