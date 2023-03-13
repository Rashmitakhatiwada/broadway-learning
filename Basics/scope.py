# a=1 #global scope
#
# def summ (b,c): #b and c are arguements
#     global a #creating a global variable inside function
#     a=2
#     print("inside function", a)
#     return b+c
#
# print("outside function",a)
# summ(2,3) #2 and 3 are parameter
# print("outside function",a)

# def summ(*args):
#     c=sum(args)
#     print(c)
#     # print(type(args))
#
# summ(1)
# summ(1,2)
# summ(1,2,3)
# summ(1,2,3,4)
# summ(1,2,3,4,5)


# def summ(**kwargs):
#     # print(kwargs)
#     # print(type(kwargs))
#     return sum(kwargs.values())
#
# print(summ(a=1))
# print(summ(a=1,b=2))
# print(summ(a=1,b=2,c=3))
# print(summ(a=1,b=2,c=3,d=4))


