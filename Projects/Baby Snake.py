"""
Program: Baby Snake
--------------------
In this assignment we are going to make a baby version of the classic Atari game of Snake. It was famously shipped on the original Apple II computers as well as Nokia phones. Here is a demo with a few extensions: Baby Snake Demo  
"""

from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1 

GOAL_SIZE = 20
PLAYER_SIZE = 20

def main():
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player_x, player_y = 0, 0
    goal_x, goal_y = 360, 360
    player = canvas.create_rectangle(player_x, player_y, player_x + PLAYER_SIZE, player_y + PLAYER_SIZE, 'blue')
    goal = canvas.create_rectangle(goal_x, goal_y, goal_x + GOAL_SIZE, goal_y + GOAL_SIZE, 'red')
    while True:
        # Handle user input to move player
        key = canvas.get_last_key_press()
        if key == 'ArrowLeft':
             player_x -= PLAYER_SIZE
             canvas.moveto(player, player_x, player_y)
        elif key == 'ArrowRight':
             player_x += PLAYER_SIZE
             canvas.moveto(player, player_x, player_y)
        elif key == 'ArrowUp':
            player_y -= PLAYER_SIZE
            canvas.moveto(player, player_x, player_y)
        elif key == 'ArrowDown':
            player_y += PLAYER_SIZE
            canvas.moveto(player, player_x, player_y)
        # Check for collisions (player and goal)
        collision = is_collision(player_x, player_y, goal_x, goal_y, PLAYER_SIZE)
        if collision:
            # Move goal to a new location
            goal_x, goal_y = move_goal_to_new_location(canvas, goal, CANVAS_WIDTH, CANVAS_HEIGHT, GOAL_SIZE)
        # Control game speed
        time.sleep(DELAY)
        
def is_collision(player_x, player_y, goal_x, goal_y, size):
    if player_x == goal_x and player_y == goal_y:
        return True
    return False

def move_goal_to_new_location(canvas, goal, WIDTH, HEIGHT, size):
    new_goal_x = random.randrange(0, WIDTH - size + 1, size)
    new_goal_y = random.randrange(0, HEIGHT - size + 1, size)
    canvas.moveto(goal, new_goal_x, new_goal_y)
    return new_goal_x, new_goal_y
    
if __name__ == '__main__':
    main()
