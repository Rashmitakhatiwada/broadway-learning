"""
for i in range(10) : #it ranges from 0 to 9
    print(i)

for i in range(1,10):
    print(i)

#print even number using range
for i in range(1, 11):
    if i % 2 == 0:
        print(f"{i} is even number"  , end=" ")
    else:
        print()

#fizzbuzz

for i in range (1,31):
    if i%3==0 and i%5==0:
        print("fizzbuzz", end=" ") #end=" " to display result in single line
    elif i%3==0:
        print("fizz", end=" ")
    elif i %5==0:
        print("buzz", end=" ")
    else:
        print(i, end=" ")

for x in [1,2,'a']:
    print(x)

for x in "hey":
    print(x)

d={
    "name":"ABC",
    "age":25,
    "address": "XYZ"
}
print(list(d.keys()))
print(list(d.values()))

#looping in the dictionary keys
for key in d.keys():
    print(key)

for value in d.values():
    print(value)

for i in d: #returns keys just like d.keys() but only in loops
    print(i)

print(d.items())

for key,value in d.items():
    print(key,value)


#enumerate

a=1,2,3,4
print(list(enumerate(a))) #enemutare displays index and value

for index,value in enumerate(a):
    print(index,value) #no of loops and its value is shown


#while loop
counter=0
while counter<5:
    counter+=1
    print(counter)
"""

