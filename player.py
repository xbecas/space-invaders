"""Space Invaders - Enemy Class"""

import turtle
import random


class Player(turtle.Turtle):
    """Define enemy as Python Turtle Object"""
    
    def __init__(self):
        super().__init__()
        self.setup()
        self.spawn()

    def setup(self):
        """Configure player as Python Turtle object"""
        self.color("blue")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        
        self.player_speed = 15


    def spawn(self):
        """Set player's initial position"""
        x = 0  # random.randint(-250, 250)
        y = -250
        self.setposition(x, y)

    def move_left(self):
        """Move the player to the left"""
        x = max(self.xcor() - self.player_speed, -280)
        self.setx(x)
        

    def move_right(self):
        """Move the player to the right"""
        x = min(self.xcor() + self.player_speed, 280)
        self.setx(x)
