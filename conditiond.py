a = int(input("enter the value of a "))
b = int(input("enter the value of b "))
c = int(input("enter the value of c "))

if a > b and a > c:
    print(f"{a} is the greatest")

elif b > c and b > a:
    print(f"{b} is greatest")

else:
    print(f"{c} is greatest")
