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