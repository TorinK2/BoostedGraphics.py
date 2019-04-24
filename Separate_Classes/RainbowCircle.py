from graphics import *
import math
import random

class RainbowCircle:
    
    def __init__(self, x, y, radius, num_lines=100):
        self.x = x
        self.y = y
        self.radius = radius
        self.num_lines = num_lines
        self.Circle = Circle(Point(x,y), radius)
        self.set_line_coords()
        self.set_line_colors()

    def remove_color(self):
        for line in self.Lines:
            line.setFill("black")
            line.setOutline("black")

    def undraw(self):
        self.Circle.undraw()
        for line in self.Lines:
            line.undraw()

    def draw(self, win):
        self.Circle.draw(win)
        for line in self.Lines:
            line.draw(win)
    
    def set_line_coords(self):
        self.Lines = []
        for coord in RainbowCircle.PointsInCircum(self.radius, self.num_lines):
            self.Lines.append(Line(Point(self.x, self.y),
                                   Point(coord[0] + self.x, coord[1] + self.y)))

    def set_line_colors(self):
        for line in self.Lines:
            line.setFill(color_rgb(random.randrange(255), random.randrange(255), random.randrange(255)))
            line.setOutline(color_rgb(random.randrange(255), random.randrange(255), random.randrange(255)))

    @staticmethod
    def PointsInCircum(self, r,n=100):
        pi = math.pi
        return [(math.cos(2*pi/n*x)*r,math.sin(2*pi/n*x)*r) for x in range(0,n+1)]


