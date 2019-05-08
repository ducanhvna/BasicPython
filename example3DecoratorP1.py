# Decorators 
# functions and method are called callable as they can be called
# Infact , any object which implements the special method __call__() is termmed callable. So, in the most basic sense, adecorator is a callable that returns a callable
# Basically, a decorator takes in a function, adds some functionality and returns it

def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

@make_pretty
def ordinary():
    print("I am ordinary")

def smart_devide(func):
    def inner(a,b):
        print("I am going to divide", a, "and", b)
        if b== 0:
            print("Whoops! cannot devide")
            return
        return func(a,b)
    return inner

@smart_devide
def divide(a,b):
    return a/b