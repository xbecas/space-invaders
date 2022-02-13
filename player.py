"""Space Invaders - Enemy Class"""

import turtle

from game import Game


game = Game()


class Player(turtle.Turtle):
    """Define enemy as Python Turtle Object"""
    
    def __init__(self):
        super().__init__()
        self.setup()
        self.spawn()

    def setup(self):
        """Configure player as Python Turtle object"""
        self.color('blue')
        self.shape('triangle')
        self.penup()
        self.speed(0)
        self.setheading(90)
        
        self.player_dx = game.get_player_dx()


    def spawn(self):
        """Set player's initial position"""
        self.setposition(game.PLAYER_INITIAL_POSITION)

    def move_left(self):
        """Move the player to the left"""
        x = max(self.xcor() - self.player_dx, game.ENEMY_MOVE_MIN_X)
        self.setx(x)
        

    def move_right(self):
        """Move the player to the right"""
        x = min(self.xcor() + self.player_dx, game.ENEMY_MOVE_MAX_X)
        self.setx(x)
