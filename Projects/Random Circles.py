"""
Program: Random Circles
--------------------
Write a program that draws a 20 circles at random positions with random colors on the canvas. You are provided with the constants N_CIRCLES (the number of circles to draw), CANVAS_WIDTH and CANVAS_HEIGHT (the width and height of the canvas, respectively) and CIRCLE_SIZE  (the width and height of each circle respectively).
"""

from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
N_CIRCLES = 20

def main():
     print('Random Circles')
     canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
     for i in range(random_n_circles()):
         draw_random_circles(canvas)
    
def random_color():
    colors = ['orange', 'deeppink', 'plum', 'lightblue', 
    'purple', 'forestgreen', 'gold', 'yellowgreen', 'salmon',
    'tan', 'navy', 'maroon', 'dimgrey', 'peachpuff', 'lightgrey',
    'teal', 'crimson']
    return random.choice(colors)
    
def circle_size():
    sz = random.randint(10, 70) # All possible sizes
    return(sz)

def random_n_circles():
    n_circles = random.randint(1, 50) # At least one circle
    return(n_circles)
    
def draw_random_circles(canvas):
    size = circle_size()
    color = random_color()
    x = random.uniform(0, 240) # x coordinates
    y = random.uniform(0, 240) # y coordinates
    right_x = x + size
    bottom_y = y + size
    canvas.create_oval(x, y, right_x, bottom_y, color)
    
    
if __name__ == '__main__':
    main()
