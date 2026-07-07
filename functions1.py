import functools
import functions
import time
def valid(func):
    @functools.wraps(func)
    def inner(a,b):
        if isinstance(a,str):
            a = str(a)
        if isinstance(b,str):
            b = str(b)
        return func(a,b)
    return inner
def fun(a:str, b:str)-> str:
    """This is a docstring
    This function is for string concatenation"""
    return a+b
print(fun.__name__)
print(fun("12","13"))
print(fun(20,30))
print(fun.__annotations__)
print(fun.__doc__)
#print(print.__doc__)

