#GGS 650
#Written in Python 2.7. I have not installed 3.7 yet.

#Assignment 2-2 compute absolute value
def absolute(x):
    if x < 0:
        result = -x
    return result

#Assignment 2-2 compute area from radius
def radius(x):
    result = x * x
    result = result * 3.14
    return result

#Assignment 2-2 compute factorial
def factorial(x):
    result = x
    fac = x - 1
    while fac > 0:
        result = result * fac
        fac = fac - 1
    return result

#Assignment 2-4 invert a list
def invert(x):
    new = []
    for i in reversed(x):
        new.append(i)
        print i
        return new

#Assignment 2-5 sort a list
def sort(x):
    new = []
    while len(new) < len(x):
        check = 1000
        for i in x:
            if i < check and i not in new:
                check = i
        new.append(check)
    return new

lis = [6, 3, 2, 8, 5]
print radius(2)
print absolute(-5)
print factorial(6)
print sort(lis)
print invert(lis)
