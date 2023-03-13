def func(name):
    return 'hello'

def greet(my_func):
    message = my_func('jane')
    print(message)

greet(func)