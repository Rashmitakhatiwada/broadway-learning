#write a python program to calculate distance between (x1,y1) and (x2,y2)

x1= int(input("enter the value of x1"))

y1= int(input("enter the value of y1"))

x2= int(input("enter the value of x2"))

y2= int(input("enter the value of y2"))

d= ((x2-x1)**2 + (y2-y1)**2)**1/2
print(int(d))

#testing weather a passed letter is a vowel or not


vowel = "a,e,i,o,u"
list = input("enter a letter")
if list.lower() in vowel:
    print("it is a vowel")
else :
    print("it is not a vowel")


#sum of given two integer and if the value is inbetween 15 and 20 print 20

first= int(input("enter the first value"))
second = int(input("enter the second value"))
total = first+second

if sum in range(16, 20):
    print("20")
else:
    print(int(total))