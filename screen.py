"""Python Turtle Screen, Canvas and Borders"""

import turtle


def is_2d_array_of_numbers(array):
    """Argument is array (list or tuple) of numbers (int or float) has
    exactly 2 dimensions"""

    if not isinstance(array, (list, tuple)):
        raise f'GameScreen: size is a {type(array)} - list or tuple expected.'

    if not len(array) == 2:
        raise f'GameScreen: size has {len(array)} elements -  2 expected.'

    if not all((isinstance(v, (float, int)) for v in array)):
        raise f'GameScreen: size elements are not floats or integers.'

    return True


class GameWindow(turtle._Screen):
    """Define enemy as Python Turtle Object"""

    CANVAS_WIDTH = 600
    CANVAS_HEIGHT = 600

    def __init__(self, title, bgcolor, size=None):
        super().__init__()
        
        turtle.TurtleScreen.__init__(self, GameWindow._canvas)
        
        if turtle.Turtle._screen is None:
            turtle.Turtle._screen = self

        # Configure Screen
        if not size:
            size = (self.CANVAS_WIDTH, self.CANVAS_HEIGHT)

        self.set_screen_size(size)
        self.set_background_color(bgcolor)
        self.set_title(title)

        draw_border(size)


    def set_screen_size(self, size):
        """Define screen size, color and title"""

        if is_2d_array_of_numbers(size):
            self.screensize(*size)


    def set_background_color(self, bgcolor):
        """Set window background color"""
        self.bgcolor(bgcolor)


    def set_title(self, title):
        """Set window title"""
        self.title = title
        
    def game_over(self):
        ender = turtle.Turtle()
        ender.hideturtle()
        ender.setposition(0, 0)
        ender.pencolor('white')
        ender.write('Game over', font=('arial',50,'bold'), align='center')
 


def draw_border(size, pen_color='white', pen_width=3):
    """Draw a border an the canvas"""

    if is_2d_array_of_numbers(size):
        canvas_width, canvas_height = size

    # Create and configure turtle
    border_pen = turtle.Turtle()
    border_pen.hideturtle()
    border_pen.speed(0)
    border_pen.color(pen_color)
    border_pen.pensize(pen_width)

    # Draw border's rectangle
    border_pen.penup()
    border_pen.setposition(-canvas_width/2,-canvas_height/2)
    border_pen.pendown()
    border_pen.setposition( canvas_width/2,-canvas_height/2)
    border_pen.setposition( canvas_width/2, canvas_height/2)
    border_pen.setposition(-canvas_width/2, canvas_height/2)
    border_pen.setposition(-canvas_width/2,-canvas_height/2)


if __name__ == '__main__':
    SIZE = CANVAS_WIDTH, CANVAS_HEIGHT = (600, 600)
    wn = GameWindow(title='Space Invaders', bgcolor='black', size=SIZE)
    draw_border(SIZE)
    wn.game_over()
    turtle.mainloop()