def split(x):
    lis = []
    if x > 100 and x < 1000:
        first = x // 100
        second = x % 100
        second = second // 10
        third = x % 10
        lis.append(first)
        lis.append(second)
        lis.append(third)
        return lis
    elif x < 100 and x > 10:
        first = x // 10
        second = x % 10
        lis.append(first)
        lis.append(second)
        return lis
    elif x < 10:
        lis.append(x)
        return lis
print (split(689))
