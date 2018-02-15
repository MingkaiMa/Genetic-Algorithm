import random

class City():
    def __init__(self, x, y):
        #self.x = random.randint(1, 200)
        #self.y = random.randint(1, 200)

        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y

    def __str__(self):
        s = ''
        s += 'City: ('
        s += str(self.x) + ',' + str(self.y) + ')'

        return s

    def __repr__(self):
        s = ''
        s += 'City: ('
        s += str(self.x) + ',' + str(self.y) + ')'

        return s

