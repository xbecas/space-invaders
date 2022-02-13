"""Space Invaders game - made with Python Turtle
Source code: https://gist.github.com/TGNYC/40f814389ba35fdf41b41858f7ce6cae
Adapted by https://github.com/xbecas
2022-02-06, Lisboa, Portugal
"""

import turtle
import math
import random

from enemies import Enemies
from bullet import Bullet
from collisions import is_collision
from screen import GameWindow

# Set up the screen
SIZE = CANVAS_WIDTH, CANVAS_HEIGHT = (600, 600)
wn = GameWindow(title='Space Invaders', bgcolor='black', size=SIZE)

# Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setheading(90)
player.setposition(0, -250)

playerspeed = 15


# Move the player left and right
def move_left():
	x = player.xcor()
	x -= playerspeed
	if x < -280:
		x = - 280
	player.setx(x)
	

def move_right():
	x = player.xcor()
	x += playerspeed
	if x > 280:
		x = 280
	player.setx(x)
	

enemies = Enemies.generate_list_of_enemies()
bullet = Bullet()


def player_fire():
	bullet.fire(player.pos())


# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(player_fire, "space")


# Main game loop
while True:
	
	for enemy in enemies:
		# Move the enemy
		enemy.update_position()
  
		# Move the enemy back and down
		if enemy.xcor() > 280 or enemy.xcor() < -280:
			enemy.move_down()

		# Check for a collision between the bullet and the enemy
		if is_collision(bullet, enemy):
			bullet.reset()		
			enemy.spawn()
		
		if is_collision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break
	
	# Move the bullet
	if bullet.state == "fire":
		bullet.update_position()
	
	# Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.reset()


# Temporary Exit Statement
wn.exitonclick()