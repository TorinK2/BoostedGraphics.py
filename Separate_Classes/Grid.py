from graphics import *
class Grid:

    def __init__(self, x,y, width, height, x_divs, y_divs):
        self.Lines = []
        x_current = x
        x_inc = width / float(x_divs)
        while(x_current<=x+width):
            self.Lines.append(Line(Point(x_current, y), Point(x_current, y+height)))
            x_current += x_inc
        y_current = y
        y_inc = height / float(y_divs)
        while(y_current<=y+height):
            self.Lines.append(Line(Point(x, y_current), Point(x+width, y_current)))
            y_current += y_inc   

    def draw(self, win):
        for line in self.Lines:
            line.draw(win)

    def undraw(self):
        for line in self.Lines:
            line.undraw()

