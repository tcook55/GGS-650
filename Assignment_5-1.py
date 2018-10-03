'''
5-1 before it is integrated with the class
The actual parameter values are 67, 44, and 95 for the Student 'Bob'
def total_score(assign, mid, proj):
    assign_perc = assign / 82
    mid_perc = mid / 50
    proj_perc = proj / 100
    result = (0.3 * assign_perc) + (0.3 * mid_perc) + (0.4 * proj_perc)
    return result
'''

#Function integrated with class
def total_score(x):
    assign_perc = x.assignment / 82
    mid_perc = x.midterm / 50
    proj_perc = x.project / 100
    result = (0.3 * assign_perc) + (0.3 * mid_perc) + (0.4 * proj_perc)
    return result

#Creating a student object taking 3 parameters
class Student:
    def __init__(self, assignment_points, midterm_points, project_score):
        self.assignment = assignment_points
        self.midterm = midterm_points
        self.project = project_score

Bob = Student(67, 44, 95)
print(total_score(Bob))

