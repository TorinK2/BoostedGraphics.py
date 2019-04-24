from graphics import *
class Stickman:

    def __init__(self, x, y, scale_factor):
        self.HeadCircle = Circle(Point(x,y), 1*scale_factor)
        self.Body = Line(Point(x, y+1*scale_factor), Point(x, y+4*scale_factor))
        self.LeftLeg = Line(Point(x, y+4*scale_factor),
                              Point(x-1*scale_factor, y+6*scale_factor))
        self.RightLeg = Line(Point(x, y+4*scale_factor),
                              Point(x+1*scale_factor, y+6*scale_factor))
        self.LeftArm = Line(Point(x, y+2*scale_factor),
                            Point(x-scale_factor*1, y+2*scale_factor))
        self.RightArm = Line(Point(x, y+2*scale_factor),
                            Point(x+scale_factor*1, y+2*scale_factor))

    def undraw(self):
        self.HeadCircle.undraw()
        self.Body.undraw()
        self.LeftLeg.undraw()
        self.RightLeg.undraw()
        self.LeftArm.undraw()
        self.RightArm.undraw()

    def draw(self, win):
        self.HeadCircle.draw(win)
        self.Body.draw(win)
        self.LeftLeg.draw(win)
        self.RightLeg.draw(win)
        self.LeftArm.draw(win)
        self.RightArm.draw(win)

