"""Space Invaders game - made with Python Turtle
Source code: https://gist.github.com/TGNYC/40f814389ba35fdf41b41858f7ce6cae
Adapted by https://github.com/xbecas
2022-02-06, Lisboa, Portugal
"""

import turtle
import math
import random

#Set up the screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invaders")

#Draw border
border_pen = turtle.Turtle()
border_pen.speed(0)
border_pen.color("white")
border_pen.penup()

border_pen.setposition(-300,-300)
border_pen.pendown()
border_pen.pensize(3)
for side in range(4):
	border_pen.fd(600)
	border_pen.lt(90)
border_pen.hideturtle()	

#Create the player turtle
player = turtle.Turtle()
player.color("blue")
player.shape("triangle")
player.penup()
player.speed(0)
player.setposition(0, -250)
player.setheading(90)

playerspeed = 15

enemyspeed = 2


def setup_enemy(enemy):
	enemy.color("red")
	enemy.shape("circle")
	enemy.penup()
	enemy.speed(0)


def spawn_enemy(enemy):
	x = random.randint(-200, 200)
	y = random.randint(100, 250)
	enemy.setposition(x, y)


def generate_list_of_enemies(number_of_enemies=5):
	"""Create list of enemies. Each enemy is a turtle object with given
	attributes, namely shape, color, speed and position
	"""	
	enemies = []

	for i in range(number_of_enemies):
		enemies.append(turtle.Turtle())

	for enemy in enemies:
		setup_enemy(enemy)
		spawn_enemy(enemy)

	return enemies


#Create the player's bullet
bullet = turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5, 0.5)
bullet.hideturtle()

bulletspeed = 20

#Define bullet state
#ready - ready to fire
#fire - bullet is firing
bulletstate = "ready"


#Move the player left and right
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
	

def fire_bullet():
	# Declare bulletstate as a global if it needs changed
	global bulletstate
	if bulletstate == "ready":
		bulletstate = "fire"
		# Move the bullet to the just above the player
		x = player.xcor()
		y = player.ycor() + 10
		bullet.setposition(x, y)
		bullet.showturtle()

def isCollision(t1, t2):
	distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
	if distance < 15:
		return True
	else:
		return False


# Create keyboard bindings
turtle.listen()
turtle.onkey(move_left, "Left")
turtle.onkey(move_right, "Right")
turtle.onkey(fire_bullet, "space")

enemies = generate_list_of_enemies()

# Main game loop
while True:
	
	for enemy in enemies:
		#Move the enemy
		x = enemy.xcor()
		x += enemyspeed
		enemy.setx(x)

		#Move the enemy back and down
		if enemy.xcor() > 280:
			y = enemy.ycor()
			y -= 40
			enemyspeed *= -1
			enemy.sety(y)

		if enemy.xcor() < -280:
			y = enemy.ycor()
			y -= 40
			enemyspeed *= -1
			enemy.sety(y)
			
		# Check for a collision between the bullet and the enemy
		if isCollision(bullet, enemy):
			# Reset the bullet
			bullet.hideturtle()
			bulletstate = "ready"
			bullet.setposition(0, -400)
			
   			# Reset the enemy
			spawn_enemy(enemy)
		
		if isCollision(player, enemy):
			player.hideturtle()
			enemy.hideturtle()
			print ("Game Over")
			break
	
	#Move the bullet
	if bulletstate == "fire":
		y = bullet.ycor()
		y += bulletspeed
		bullet.sety(y)
	
	#Check to see if the bullet has gone to the top
	if bullet.ycor() > 275:
		bullet.hideturtle()
		bulletstate = "ready"


# Temporary Exit Statement
wn.exitonclick()