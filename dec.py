def validate_positive(func):
    def inner(*args):
        for i in args:
            if i<0:
                print("bro")
                return
        return func(*args)
    return inner
@validate_positive
def multiply(a,b):

    return a*b
print(multiply(1,2))
print(multiply(-10,12))
def my_decorator(func):
    def wrapper(*args,**kwargs):
        print("Before")
        result=func(*args,**kwargs)
        print("After")
        return result
    return wrapper
def my_decorator(func):
    def wrapper(*args, **kwargs):
        print("Function is starting")
        result = func(*args, **kwargs)
        print("Function is done")
        return result
    return wrapper
@my_decorator
def greet():
    print("Hello!")
greet()
def my_decorator(func):
    def wrapper(*args, **kwargs):   # ← why these matter
        print("Starting")
        result = func(*args, **kwargs)  # ← passed straight through
        print("Done")
        return result
    return wrapper
def decorator_plain(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
@decorator_plain
def say_hello():
    print("Hello!")
print(say_hello.__name__)
print(say_hello.__doc__)
def decorator_wraps(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
        return wrapper

@decorator_wraps
def say_hello():
    print("Hello!")
print(say_hello.__name__)
print(say_hello.__doc__)


