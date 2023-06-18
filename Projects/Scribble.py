"""
Program: Scribble
--------------------
You job is to write a program that draws a circle wherever the mouse is located on the screen. The user will move their mouse within the canvas, and a circle should be drawn with its left and top x and y values as the x and y values of the user's mouse. 
"""
from graphics import Canvas
import random

CANVAS_WIDTH = 300
CANVAS_HEIGHT = 300
CIRCLE_SIZE = 20
DELAY = 0.01

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    while True:
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        ball = draw_circle(canvas, mouse_x, mouse_y)
        time.sleep(DELAY)

   
def random_color():
    colors = ['orange', 'deeppink', 'plum', 'lightblue', 
    'purple', 'forestgreen', 'gold', 'yellowgreen', 'salmon',
    'tan', 'navy', 'maroon', 'dimgrey', 'peachpuff', 'lightgrey',
    'teal', 'crimson']
    return random.choice(colors)

def draw_circle(canvas, start_x, start_y):
    size = CIRCLE_SIZE
    color = random_color()
    right_x = start_x + size
    bottom_y = start_y + size
    canvas.create_oval(start_x, start_y, right_x, bottom_y, color)    

if __name__ == "__main__":
    main()
