from turtle import Turtle
import random

STARTING_COORD = (0, 50)
HEADING_START = random.randint(205, 330)
SPEED = 10


class Ball(Turtle):
    """Creates a white round ball"""
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(STARTING_COORD)
        self.color("white")
        self.shape("circle")
        self.speed = SPEED
        self.setheading(HEADING_START)

    def move(self):
        """Movese the ball forward"""
        self.forward(self.speed)

    def bounce_side(self):
        # self.setheading(self.heading() * -1)
        self.setheading(180 - self.heading())

    def bounce(self):
        # self.setheading(90 - self.heading())
        self.setheading(self.heading() * -1)

    def reset(self):
        """Resets the ball on initial position with randomized heading"""
        last_direction = self.heading()
        self.goto(STARTING_COORD)
        self.speed = SPEED
        self.setheading(random.randint(205, 330))