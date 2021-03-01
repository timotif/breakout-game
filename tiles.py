from turtle import Turtle
import turtle
import random

TILE_SIZE = 5
TILE_PX = TILE_SIZE * 20
STARTING_X = -turtle.screensize()[0] + TILE_PX/2
STARTING_Y = turtle.screensize()[1] - 50
COLORS = ['red', 'green', 'blue', 'yellow', 'purple']


class Tile(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.color('white')
        self.goto(0, 0)
        self.shape('square')
        self.shapesize(stretch_len=TILE_SIZE, stretch_wid=1)


class Row():
    def __init__(self, n):
        self.tiles = []
        self.create_wall(n)

    def create_wall(self,n):
        screen_size = turtle.screensize()
        y = STARTING_Y - n*23
        tiles_row = 2 * screen_size[0] // TILE_PX
        old_color = random.choice(COLORS)
        for i in range(tiles_row):
            color = random.choice(COLORS)
            while color == old_color:
                color = random.choice(COLORS)
            old_color = color
            new_tile = Tile()
            new_tile.goto(STARTING_X + i*TILE_PX, y)
            new_tile.color(color)
            self.add_tile(new_tile)
            print(f"Tile n. {i}, x={STARTING_X + i * TILE_PX}, color: {color}")

    def add_tile(self, new_tile):
        self.tiles.append(new_tile)