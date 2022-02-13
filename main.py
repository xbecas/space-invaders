"""Space Invaders game - made with Python Turtle
Source code: https://gist.github.com/TGNYC/40f814389ba35fdf41b41858f7ce6cae
Adapted by https://github.com/xbecas
2022-02-06, Lisboa, Portugal
"""

import turtle

from player import Player
from enemies import Enemies
from bullet import Bullet
from collisions import is_collision
from screen import GameWindow
from game import Game
from config import GameConfig


config = GameConfig()

# Set up the screen
wn = GameWindow(
    title=config.TITLE,
    bgcolor=config.BACKGROUND_COLOR,
    size=(config.CANVAS_WIDTH, config.CANVAS_HEIGHT)
    )

game = Game()
player = Player()
bullet = Bullet()
enemies = Enemies.generate_list_of_enemies(game.number_of_enemies)


def player_move_left():
    """Move player's ship to the left"""
    player.move_left()


def player_move_right():
    """Move player's ship to the right"""
    player.move_right()


def player_fire():
    """Fire bullet from player's ship"""
    bullet.fire(player.pos())


def game_over():
    """Sorry... you lost! But you can always try again!"""
    # [t.hideturtle() for t in wn.turtles()]
    print('Exit using "q" key')
    wn.show_game_over()
    game.game_over()


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
        if enemy.reached_goal() or is_collision(player, enemy):
            keep_playing = False
            game_over()
            break

        # Check for a collision between the bullet and the enemy
        if is_collision(bullet, enemy):
            bullet.reset()
            enemy.spawn()


# Click on windows `close button` to exit
wn.exitonclick()