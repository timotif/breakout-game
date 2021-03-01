import turtle
from turtle import Screen
from paddle import Paddle
from ball import *
from tiles import *
from scoreboard import *
import time

WALL_DEPTH = 3

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor('black')
screen.title('My Breakout game')
screen.tracer(0)
paddle = Paddle()

screen.listen()
screen.onkey(paddle.move_left, 'Left')
screen.onkey(paddle.move_right, 'Right')

ball = Ball()

scoreboard = Scoreboard()

# control_tile = Tile()
wall_tiles = []
for i in range(WALL_DEPTH):
    new_row = Row(i)
    for tile in new_row.tiles:
        wall_tiles.append(tile)
print(len(wall_tiles))
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.04)
    ball.move()
    # print(ball.xcor())

    # Detect collision with paddle and top margin
    if ball.distance(paddle) < 50 and ball.ycor() < -230 or ball.ycor() > scoreboard.end_header:
        # print("Made contact")
        ball.bounce()

    # Detect collision with wall
    if ball.xcor() < -380 or ball.xcor() > 380:
        # print('Wall bounce')
        ball.bounce_side()

    # Detect collision with tile
    for tile in wall_tiles:
        if ball.distance(tile) < 55:
            ball.bounce()
            tile.goto(1000, 1000)
            wall_tiles.remove(tile)
            screen.update()
            # print(len(wall_tiles))
            scoreboard.point()

    # Detect missed ball
    if ball.ycor() < -295:
        scoreboard.lives()
        ball.reset()

    # Detect game over
    if len(wall_tiles) == 0 or scoreboard.credits == 0:
        scoreboard.game_over()
        game_is_on = False



screen.exitonclick()

