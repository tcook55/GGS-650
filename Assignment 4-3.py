#4-3 a
class TempSample:
    def __init__(self, new_x, new_y, t):
        self.x = new_x
        self.y = new_y
        self.temp = t
    #4-3 b
    def heat_up(self, heat):
        self.temp += heat
#4-3 c
def average_temp(samples):
    temperatures = []
    total = 0
    for x in samples:
        total += x.temp
        temperatures.append(x.temp)
    result = total // len(temperatures)
    return result
    


my_sample1 = TempSample(6, 4, 31)
my_sample2 = TempSample(8, 8, 25)
my_sample3 = TempSample(3, 7, 34)
all_samples = [my_sample1, my_sample2, my_sample3]

#my_sample1.heat_up(5)
print (my_sample1.temp)
print (average_temp(all_samples))
