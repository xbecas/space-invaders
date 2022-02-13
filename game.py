"""Space Invaders game - made with Python Turtle
Game logic and level variables"""


import random
import time
import sys

from config import GameConfig


config = GameConfig()


class Game():

    PLAYER_INITIAL_POSITION = config.PLAYER_INITIAL_POSITION
    PLAYER_INITIAL_DX = config.PLAYER_INITIAL_DX
    
    ENEMY_MOVE_MIN_X = config.CANVAS_LIMIT_LEFT
    ENEMY_MOVE_MAX_X = config.CANVAS_LIMIT_RIGHT
    ENEMY_SPAWN_MIN_Y = config.ENEMY_SPAWN_MIN_Y
    ENEMY_SPAWN_MAX_Y = config.ENEMY_SPAWN_MAX_Y
    ENEMY_DX = config.ENEMY_DX
    ENEMY_DY = config.ENEMY_DY
    ENEMY_Y_GOAL = config.ENEMY_Y_GOAL
    
    def __init__(self):
        self.number_of_enemies = config.ENEMIES_INITIAL_NUMBER
        self.keep_playing = True
    
    
    def get_enemy_position(self):
        x = random.randint(self.ENEMY_MOVE_MIN_X, self.ENEMY_MOVE_MAX_X)
        y = random.randint(self.ENEMY_SPAWN_MIN_Y, self.ENEMY_SPAWN_MAX_Y)
        return (x, y)
    
    def get_enemy_speed(self):
        """Enemy's speed will change over time during gameplay"""
        return self.ENEMY_DX  # random.randint(2, 5)

    
    def get_player_dx(self):
        """Player's lateral movement will change over time during gameplay"""
        return self.PLAYER_INITIAL_DX
    
    
    @staticmethod
    def game_over():
        time.sleep(2)
        sys.exit('Game over')

