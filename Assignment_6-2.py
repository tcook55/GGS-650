import math

#open text file
file = open('C:/Users/Tyler/Documents/Classes/Fall 2018/GGS_650/Module_6/text.txt')
#Put each line into a list
lines = file.readlines()

#Create object list. Variable name doesn't matter they will all be labeled 'point'
#each index will be a point class that I will pull from to do calculations.
points = []

#Create point class taking x and y as attributes
class Point:
    def __init__(self, x_point, y_point):
        self.x = x_point
        self.y = y_point

#Iterate through text file splitting values at "," and turning them into floats.
#Put each xy pair into a point object and append that object to the points list
for line in lines:
    split = line.split(",")
    point = Point(float(split[0]), float(split[1]))
    print(float(split[0]), float(split[1]))
    points.append(point)


#Iterate through points list calculating distance between points
ctr = 0
distance = 0
while ctr < len(points) - 1:
    ctr2 = ctr + 1
    seg_dist = math.hypot(points[ctr2].x - points[ctr].x, points[ctr2].y - points[ctr].y)
    distance += seg_dist
    ctr += 1
#Return polyline distance
print("Polyline distance length: " + str(distance))

file.close()
