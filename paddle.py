from turtle import Turtle

# variables for the game:
move_distance = 4
up = 90
down = 270

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.shapesize (stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def down(self):
        x_stays_the_same = self.xcor ()
        new_y = self.ycor () - 20
        self.goto (x_stays_the_same, new_y)

    def up(self):
        x_stays_the_same = self.xcor()
        new_y = self.ycor() + 20
        self.goto(x_stays_the_same, new_y)