#4-2 a
class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
#4-2 b
class LineSegment:
    def __init__(self, start, end):
        self.start_point = start
        self.end_point = end

#4-2 c
def rhs(a, b, c):
    originx = a.x
    originy = a.y
    b.x -= originx
    b.y -= originy
    c.x -= originx
    c.y -= originy
    result = (b.x * c.y) - (b.y * c.x)
    if result < 0:
        return 1
    elif result == 0:
        return 0
    else:
        return -1

#4-2 d
def cross(a, b):
    originx = a.start_point.x
    originy = a.start_point.y
    a.end_point.x -= originx
    a.end_point.y -= originy
    b.start_point.x -= originx
    b.start_point.y -= originy
    b.end_point.x -= originx
    b.end_point.y -= originy
    check_start = (a.end_point.x * b.start_point.y) - (a.end_point.y * b.start_point.x)
    check_end = (a.end_point.x * b.end_point.y) - (a.end_point.y * b.end_point.x)

    if check_start > 0 and check_end > 0:
        return 0
    elif check_start < 0 and check_end < 0:
        return 0
    else:
        return 1
    
my_point1 = Point(0,5)
my_point2 = Point(9,13)
my_point3 = Point(1,6)
my_point4 = Point(7,2)

line1 = LineSegment(my_point1, my_point2)
line2 = LineSegment(my_point3, my_point4)


print (cross(line1, line2))
print (rhs(my_point1, my_point2, my_point3))
