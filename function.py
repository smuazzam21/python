
def fun1():
    print("Hello")
    f2()
    print("Exiting fun1")

def f2():
    print("Hello - F2")
    print("Exiting F2")

def f1(a1):
    print(type(a1))
    print(a1)

def fun2(a1=10):
    print("IN FUN2")
    print(a1)

def f3(**kwargs):
    print(type(kwargs))
    print(len(kwargs))

print("Start")
f3(K1=10,K2=20)
print("Back")

