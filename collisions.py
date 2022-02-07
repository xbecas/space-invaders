import math

def is_collision(t1, t2):
    """Check for collision between two Turtle objects: t1 and t2."""
    distance = math.sqrt(
        math.pow(t1.xcor() - t2.xcor(), 2) + 
        math.pow(t1.ycor() - t2.ycor(), 2)
        )
    return True if distance < 15 else False
