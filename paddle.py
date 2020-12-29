from turtle import Turtle

# variables for the game:
move_distance = 4
up = 90
down = 270

class Paddle:
    def __init__(self, position):
        self.paddle = self.create_paddle(position)

    def create_paddle(self, position):
        paddle = Turtle(shape='square')
        paddle.color('white')
        paddle.penup()
        paddle.shapesize(stretch_wid = 5, stretch_len = 1)
        paddle.goto(position)
        return paddle

    def down(self):
        x_stays_the_same = self.paddle.xcor ()
        new_y = self.paddle.ycor () - 20
        self.paddle.goto (x_stays_the_same, new_y)

    def up(self):
        x_stays_the_same = self.paddle.xcor()
        new_y = self.paddle.ycor() + 20
        self.paddle.goto(x_stays_the_same, new_y)