import copy # Changes made to a copy of an object affects the original object
import random
# Consider using the modules imported above.
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for i in range(num_experiments):
        expected_copy = copy.deepcopy(expected_balls)
        hat_copy = copy.deepcopy(hat)
        colors = hat_copy.draw(num_balls_drawn)
        for i in colors:
            if i in expected_copy:
                expected_copy[i] -= 1
        if all (x <= 0 for x in expected_copy.values()):
            count += 1
    return count / num_experiments
class Hat:
    def __init__(self, **balls): # **: variable number of inputs
        # **balls: dict of the form {'color1':number of balls, 'color2':number of balls, ...}
        self.contents = []
        for key, value in balls.items():
            for i in range(value):
                self.contents.append(key)
                # The colors in the list are already repeated
    def draw(self, number):
        if number > len(self.contents):
            return self.contents
        else:
            removed_lst = []
            for i in range(number):
                removed_obj = self.contents.pop(random.randint(0,len(self.contents)-1))
                removed_lst.append(removed_obj)
            return removed_lst
hat = Hat(blue=6, red=3, green=3)
probability = experiment(hat, {"red": 2, "green":1}, 6, 3000)
print(probability)
