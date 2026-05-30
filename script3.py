def fun(x,y):
    print(x,y)
    return x+y
print(fun(10,20))
def great(a,b):
    if a>b:
        return a
    else:
        return b
print(great(75,77))
def f1(*a):
    return sum(a)
x = f1(1,7,8,6,5,3,2,8)
print(x)
if (x & 1):
    print("odd")
else:
    print("even")
def fun4(x,y):
    print (x+y)
print(fun4(1,2))
a = 7
l = f"a:{a**a}"
print(l)