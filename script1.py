def fun(x,y):
    print(x,y)
    return x+y
print(fun(10,20))
def great (a,b):
    if a>b:
        return a
    else:
        return b
print(great(75,77))
def value(*a):
    return sum(a)
fun=value(1,7,8,6,5,3,2,8)
print(fun)
if(fun%2==0):
    print("even")
else:
    print("odd")

def fun5 (x,y):
    print(x+y)
z=fun5
k=(z(10,45))
print(z)


