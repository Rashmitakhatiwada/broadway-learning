#create a class department with parameter name and no of students. creatae a method total students which takes
# object as a parameter and return total no of students from all departments

from functools import reduce
class Department:
    def __init__(self, name, no_of_students):
        self.name = name
        self.no_of_students = no_of_students

    def total(self, *args ):
        # return self.no_of_students + .no_of_students

        list_of_nums = [i.no_of_students for i in args]
        other_total=sum(list_of_nums)
        return self.no_of_students + other_total

d1 = Department("dept1", 30)
d2 = Department("dept2", 20)
d3 = Department("dept2", 10)
d4 = Department("dept2", 5)
result= d1.total(d2, d3, d4)
print(result)