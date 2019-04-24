from boostedgraphics import *

'''
Code written by Torin Kovach in April 2019
'''
win = GraphWin("Test", 500, 500)

test_grid = Grid(50,50,100,100,10,5)
test_grid.draw(win)

test_rcircle = RainbowCircle(300, 300, 100, 500)
test_rcircle.draw(win)

test_stickman = Stickman(400, 50, 30)
test_stickman.draw(win)

for item in [test_rcircle, test_grid, test_stickman]:
    item.undraw()

win.close()
