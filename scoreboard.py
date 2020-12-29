from turtle import Turtle

import random
# Create our food class which is inherited from the Turtle Class
# Now, this food is like when we create our Turtle but we're customizing it.


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.l_score = 0
        self.r_score = 0
        self.goto (-100, 200)
        self.write(f"{self.l_score}", True, align="center", font=('Courier', 60, 'bold'))
        self.goto (100, 200)
        self.write (f"{self.r_score}", True, align="center", font=('Courier', 60, 'bold'))

    def score_points_left(self):
        self.l_score += 1
        self.clear ()
        self.goto (-100, 200)
        self.write (f"{self.l_score}", True, align="center", font=('Courier', 60, 'bold'))
        self.goto (100, 200)
        self.write (f"{self.r_score}", True, align="center", font=('Courier', 60, 'bold'))

    def score_points_right(self):
        self.r_score += 1
        self.clear ()
        self.goto (-100, 200)
        self.write (f"{self.r_score}", True, align="center", font=('Courier', 60, 'bold'))
        self.goto (100, 200)
        self.write (f"{self.l_score}", True, align="center", font=('Courier', 60, 'bold'))