"""Space Invaders - Enemy Class"""

import turtle
import random


class Enemy(turtle.Turtle):
    """Define enemy as Python Turtle Object"""
    
    def __init__(self):
        super().__init__()
        self.dx = 2    

    def setup(self):
        """Configure enemy as Python Turtle object"""
        self.color("red")
        self.shape("circle")
        self.penup()
        self.speed(0)


    def spawn(self):
        """Set enemy initial position"""
        x = random.randint(-200, 200)
        y = random.randint(100, 250)
        self.setposition(x, y)


class Enemies():
    """Create list of enemies. Each enemy is a turtle object with given
    attributes, namely shape, color, speed and position"""
    
    def generate_list_of_enemies(number_of_enemies=5):
        
        enemies = []
        for i in range(number_of_enemies):
            enemies.append(Enemy())

        for enemy in enemies:
            enemy.setup()
            enemy.spawn()

        return enemies


if __name__ == '__main__':
    enemies = Enemies.generate_list_of_enemies()
    turtle.mainloop()