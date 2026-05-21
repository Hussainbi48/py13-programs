def fun(*a):
    print(a)
    print(*a)
fun(10, 20, 30, 40, 50)
def fun3(a, b, c, d):
    print(a, b, c, d)
def fun2(**b):
    print(b)
    fun3(**b)
fun2(a=75, b=30, c=40, d=70)
def fun5(*a,**b):
    print(a,b,sep="\n")
fun5(10,1,7,3,8,6, a=75,b=30)
fun5(10,7,a=30,b=50)
def fun6(*a):
    i=0;s=0;
    while i<len(a):
        if a[i]%2==0:
            s+=a[i]
        i+=1
    print(s)
fun6(1,7,8,25,30,60,70)
def fun7(*a):
    i=0
    c=0
    s=0
    while i<len(a):
        if i%2==0:
            s+=a[i]
        i+=1
        c+=1

