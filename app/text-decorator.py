
def decorator(func):
    def wrapper(x):
        assert type(x) == int, "Argument must be int type"
        if x % 2 == 0:
            print("This is an even number")
            func(x)
        else:
            pass

    return wrapper


@decorator
def getnum(num):        # equiv: getnum = decorator(getnum)
    print("Finish print ", num)


getnum(10)