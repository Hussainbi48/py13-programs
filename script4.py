l= ["Hello", "Hii", "Who", "are", "you?"]
def fun(x):
    k = list(map(fun2, x))
    k = "".join(k)
    return k

def fun2(y):
    if y not in "AEIOUaeiou":
        return y
    return ""

result = list(map(fun, l))
print(result)
def fun3(x):
    k = list(filter(lambda y: y not in "AEIOUaeiou", x))
    k = "".join(k)
    return k

k = list(map(fun3, l))
print(k)