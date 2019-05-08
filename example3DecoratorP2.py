# In Python, this magic done is as function(*args, **kwargs). In this way, args will be the tuple of positional arguments and kwargs will be the dictionary of keyword arguments. An example of such decorator will be
def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner

def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner
    
@star
@percent
def printer(msg):
    print(msg)

@percent
@star
def printer2(msg):
    print (msg)

printer("Hello world")
printer2("Hello")