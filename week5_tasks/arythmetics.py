def add(a,b):
    return a+b


def substract(a,b):
    if a>b:
        return a-b
    elif a<b:
        return b-a

def divide(a,b):
    if a > b:
        return a//b
    elif a < b:
        return b//a
    

def multiply(a,b):
    return a*b

def test(a,b):
    return a == b