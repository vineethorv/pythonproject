def decoratorfunc(function):
    def wrapper():
        func = function()
        makeuppercase = func.upper()
        return makeuppercase
    return wrapper


@decoratorfunc
def sayhi():
    print("hi there")
    return "Hello World"

print(sayhi())