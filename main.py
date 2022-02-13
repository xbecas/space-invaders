"""Space Invaders game - made with Python Turtle
Source code: https://gist.github.com/TGNYC/40f814389ba35fdf41b41858f7ce6cae
Adapted by https://github.com/xbecas
2022-02-06, Lisboa, Portugal
"""

import turtle
import sys

from player import Player
from enemies import Enemies
from bullet import Bullet
from collisions import is_collision
from screen import GameWindow


# Set up the screen
SIZE = CANVAS_WIDTH, CANVAS_HEIGHT = (600, 600)
wn = GameWindow(title='Space Invaders', bgcolor='black', size=SIZE)
# turtle.tracer(0)

player = Player()
bullet = Bullet()
enemies = Enemies.generate_list_of_enemies()


# Player's moves
def player_move_left():
    player.move_left()

def player_move_right():
    player.move_right()

def player_fire():
     bullet.fire(player.pos())

def game_over():
    wn.game_over()
    sys.exit('Game over')

def game_over():
    # [t.hideturtle() for t in wn.turtles()]
    print('Exit using "q" key')
    wn.game_over()
    return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(player_move_left, "Left")
turtle.onkey(player_move_right, "Right")
turtle.onkey(player_fire, "space")
turtle.onkey(game_over, "q")


# Main game loop
keep_playing = True
while keep_playing:
    
    # Move the bullet
    bullet.update_position()

    # Move the enemies
    for enemy in enemies:
        enemy.update_position()

        # Check for a collision between the bullet and the enemy
        if is_collision(bullet, enemy):
            bullet.reset()        
            enemy.spawn()
        
        if enemy.ycor() < -210:
            keep_playing = game_over()
            break
    
#    turtle.update()

# Temporary Exit Statement
wn.exitonclick()