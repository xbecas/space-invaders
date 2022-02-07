"""Create the player's bullet"""

import turtle


class Bullet(turtle.Turtle):
    """Define bullet as Python Turtle Object.
    Bullet fired by player to hit enemies. Bullet has to states:
        # ready - ready to fire
        # fire - bullet is firing
    """
    
    def __init__(self):
        super().__init__()
        self.dy = 20    
        self.state = "ready"
        self.setup()

    
    def setup(self):
        """Configure bullet as Python Turtle object"""
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.hideturtle()


    def fire(self, pos):
        if self.state == "ready":
            self.state = "fire"
            self.setposition(pos)
            self.showturtle()
    
    
    def update_position(self):
        new_y = self.ycor() + self.dy
        self.sety(new_y)
        

    def reset(self):
        # Reset the bullet
        self.hideturtle()
        self.state = "ready"
        # self.setposition(0, -400)

