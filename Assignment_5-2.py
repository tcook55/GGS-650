class Plushy:
    def __init__(self, color):
        self.color = color
    def change_color(self, new_color):
        self.color = new_color

#Shadow is a black panther
Shadow = Plushy("Black")


#I'm white!
Fluffy = Shadow
Fluffy.change_color("White")

print("Shadow is a ", Shadow.color," plushy")
print("Fluffy is a ", Fluffy.color, " plushy")
#Why is shadow white I made her black?
#Shadow is white because the variable fluffy was assigned to the value Shadow.
#When the change color function was called it changed the value of Fluffy whic is shadow.



#Make shadow black again
Shadow.change_color("Black")
print("Shadow is a ", Shadow.color," plushy")
print("Fluffy is a ", Fluffy.color, " plushy")
#Why is fluffy black now?
#Fluffy is black now because it is the variable that represents Shadow and Shadow's
#value was changed to black

print('====================================')
print("Solution:")

Shadow = Plushy("Orange")
Fluffy = Plushy("Orange")

Fluffy.change_color("White")
Shadow.change_color("Black")

print("Shadow is a ", Shadow.color," plushy")
print("Fluffy is a ", Fluffy.color, " plushy")
