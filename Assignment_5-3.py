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
    print ("Check lines")
    for check in lines:
        if cross(check, check_line) == 1:
            print ("Start point: " + str(check.start_point.x) + ", " + str(check.start_point.y))
            print ("End point: " + str(check.end_point.x) + ", " + str(check.end_point.y))
            print ("Start point: " + str(check_line.start_point.x) + ", " + str(check_line.start_point.y))
            print ("End point: " + str(check_line.end_point.x) + ", " + str(check_line.end_point.y))

            cross_check += 1
        print (cross_check)
    if cross_check % 2 == 0:
        return 0
    else:
        return 1

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

def cross(a, b):
    '''
    print ("----------")
    print ("Start point: " + str(a.start_point.x) + ", " + str(a.start_point.y))
    print ("End point: " + str(a.end_point.x) + ", " + str(a.end_point.y))
    print ("Start point: " + str(b.start_point.x) + ", " + str(b.start_point.y))
    print ("End point: " + str(b.end_point.x) + ", " + str(b.end_point.y))
    '''
    originx = a.start_point.x
    originy = a.start_point.y
    originendx = a.end_point.x - originx
    originendy = a.end_point.y - originy
    otherstartx = b.start_point.x - originx
    otherstarty = b.start_point.y - originy
    otherendx = b.end_point.x - originx
    otherendy = b.end_point.y - originy
    check_start = (originendx * otherstarty) - (originendy * otherstartx)
    check_end = (originendx * otherendy) - (originendy * otherendx)
    print (check_start, check_end)

    if check_start > 0 and check_end > 0:
        return 0
    elif check_start < 0 and check_end < 0:
        return 0
    else:
        return 1
    
my_point1 = Point(5,1)
my_point2 = Point(6,6)
my_point3 = Point(1,5)
my_point4 = Point(-2,-3)
my_point5 = Point(5,-4)

interior_point = Point(1,1)
exterior_point = Point(25,5)

line1 = LineSegment(my_point1, my_point2)
line2 = LineSegment(my_point3, my_point4)

points = [my_point1, my_point2, my_point3, my_point4, my_point5]
poly = Polygon(points)
print (PIP(poly, interior_point))
