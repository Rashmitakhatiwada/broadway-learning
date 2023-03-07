import time
# def summ(a,b):
#     return a+b
#
#
#
# def diff(a,b):
#     return a-b
#
# print(summ(5,4))
# print(diff(5,4))


#
# def greet(msg):
#     def print_msz():
#         print(msg)
#     return print_msz
#
# msz=greet("hello world")
# msz()

# def decorate_me(func):
#     def inner_func(a,b):
#         print("it is a decorator function")
#         return func(a,b)
#     return inner_func
# @decorate_me
# def addition(a,b):
#     return a+b

# addition=decorate_me(addition)
# print(addition(2,3))

# #decorator using *args and **kwargs
# def decorate_me(func):
#     def inner_func(*args, **kwargs):
#         print("it is a decorator function")
#         return func(*args, **kwargs)
#     return inner_func
#
# @decorate_me
# def addition(a,b,c):
#     return a+b+c

# print(addition(2,3,4))

def executaion_time(func):
    def inner_func(*args,**kwargs):
        start=time.time()
        r=func(*args, **kwargs)
        end=time.time()
        print(f"execution time is {end-start}" )
        return r
    return inner_func


@executaion_time
def times():
    # for i in range(10000000):
    #     pass
    time.sleep(5)
    print("hello")

# times=executaion_time(times)
times()