from turtle import Turtle
import turtle

CREDITS = 3
SCORE_X = -turtle.screensize()[0] + 30
SCORE_Y = turtle.screensize()[1] - 30
CREDIT_X = turtle.screensize()[0] - 30
CREDIT_Y = turtle.screensize()[1] - 30
FONT_SIZE = 25

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.credits = CREDITS
        self.score = 0
        self.color('white')
        self.end_header = CREDIT_Y - FONT_SIZE/2
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(SCORE_X, SCORE_Y)
        self.write(f"SCORE: {self.score}", align="left", font=("Courier", FONT_SIZE, "normal"))
        self.goto(CREDIT_X, CREDIT_Y)
        self.write(f"CREDITS: {self.credits}", align="right", font=('Courier', FONT_SIZE, "normal"))

    def point(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def lives(self):
        self.credits -= 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=("courier", 30, "normal"))
