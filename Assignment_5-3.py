class Point:
    def __init__(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        
class LineSegment:
    def __init__(self, start, end):
        self.start_point = start
        self.end_point = end

class Polygon:
    def __init__(self, lis):
        self.points = lis

def get_LineSegments(poly):
    line_lis = []
    ctr = 0
    while ctr <= len(poly.points) - 1:
        if ctr <= len(poly.points) - 2:
            line = LineSegment(poly.points[ctr], poly.points[ctr + 1])
            line_lis.append(line)
            ctr += 1
        else:
            line = LineSegment(poly.points[ctr], poly.points[0])
            line_lis.append(line)
            ctr += 1
    return line_lis

def PIP(poly, point):
    max_x = 0
    for iter in poly.points:
        if iter.x > max_x:
            max_x = iter.x
    check_point = Point(max_x, point.y)
    check_line = LineSegment(point, check_point)
    lines = get_LineSegments(poly)
    cross_check = 0
    for check in lines:
        if cross(check, check_line) == 1:
            cross_check += 1
    if cross_check % 2 == 0:
        return 0
    else:
        return 1

def rhs(a, b, c):
    p1x = a.x
    p1y = a.y
    p2x = b.x - p1x
    p2y = b.y - p1y
    p3x = c.x - p1x
    p3y = c.y - p1y
    result = (p2x * p3y) - (p2y * p3x)
    if result < 0:
        return 1
    elif result == 0:
        return 0
    else:
        return -1

def cross(a, b):
    p1 = a.start_point
    p2 = a.end_point
    p3 = b.start_point
    p4 = b.end_point
    
    line1 = rhs(p1, p2, p3)
    line2 = rhs(p1, p2, p4)

    if line1 > 0 and line2 > 0:
        return 0
    elif line1 < 0 and line2 < 0:
        return 0
    else:
        return 1
    
my_point1 = Point(5,1)
my_point2 = Point(6,6)
my_point3 = Point(1,5)
my_point4 = Point(1, 1)

interior_point = Point(3,3)
exterior_point = Point(-25,4)

line1 = LineSegment(my_point1, my_point2)
line2 = LineSegment(my_point3, my_point4)

points = [my_point1, my_point2, my_point3, my_point4]
poly = Polygon(points)
print (PIP(poly, exterior_point))
