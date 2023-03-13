def pass_require(func):
    def inner_func(*args,**kwargs):

        b=""
        b = input("enter your password")
        a = "1234"
        if b in a:
            return func(*args, **kwargs)
        else:
            print("you do not have an excess")


    return inner_func


@pass_require
def password_check():
    print("hello world")

password_check()