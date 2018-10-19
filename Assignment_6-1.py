#Create class objects for point, rectangle, and square
class Rectangle:
    def __init__(self, pt, ln, wd):
        self.point = pt
        self.length = float(ln)
        self.width = float(wd)
    #Method for calculating area of rectangle
    def getarea(self):
        area = self.length * self.width
        return area

class Square(Rectangle):
    def __init__(self, side):
        self.length = side
        self.width = side
        
class Point:
    def __init__(self, x_point, y_point):
        self.x = x_point
        self.y = y_point

#Creating 4 variables for length, width, start point x, and start point y
ln = input("Length: ")
wd = input("Width: ")
x = input("Lower left point x value: ")
y = input("Lower left point y value: ")
#Create point object
pt = Point(x,y)

#Create rectangle object
rect = Rectangle(pt,ln,wd)
#If length and width are the same, turn rectangle into a square object
if ln == wd:
    rect = Square(pt, ln, wd)

#Call area calculation using class method
area = rect.getarea()
print(area)
