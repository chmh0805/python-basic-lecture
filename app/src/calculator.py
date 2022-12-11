def plus(x=0, y=0):
    print(x + y)

def minus(x=0, y=0):
    print(x - y)

def multiple(x=0, y=0):
    print(x * y)

def devide(x=0, y=1):
    if (y == 0):
        y = 1
    print(x / y)

def powerOf(x=0, y=0):
    print(x ** y)

plus()
minus()
multiple()
devide()
powerOf()