lis = [6, 3, 2, 8, 5]

def sort(x):
    new = []
    while len(new) < len(x):
        check = 1000
        for i in x:
            if i < check and i not in new:
                check = i
        new.append(check)
    return new

print (sort(lis))
