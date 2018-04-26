from Shared import WINDOW_HIEGHT

class Stripes:
    def __init__(self, width=20, height=80, count=20, x=0, y=-10, spacing=20, speed=4):
        self.width = width
        self.height = height
        self.count = count
        self.x = x
        self.y = y
        self.spacing = spacing
        self.speed = speed
        self.stripes = []
    
    def build(self):
        for i in range(self.count):
            self.stripes.append([self.x, self.y, self.width, self.height])
            self.y += self.height + self.spacing
        
    def move(self):
        for i in range(self.count):
            self.stripes[i][1] += self.speed
            if self.stripes[i][1] > WINDOW_HIEGHT:
                print(self.stripes[i][1])
                self.stripes[i][1] = - (self.height + self.spacing)

    def get(self):
        return self.stripes
