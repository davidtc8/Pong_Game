from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

# Creating the screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.tracer(2)
screen.title('🏓 Pong Game! 🏓')

# Calling Scoreboard
scoreboard = Scoreboard()

# Calling the Paddle Class to create 2 paddle objects
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

# Setting the listening method so we can move our paddle
screen.listen()
screen.onkey(r_paddle.up, key='Up')
screen.onkey(r_paddle.down, key='Down')
screen.onkey(l_paddle.up, key='w')
screen.onkey(l_paddle.down, key='s')

screen.update()

game_is_on = True

while game_is_on:
    time.sleep (ball.move_speed)
    screen.update ()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce_y()

    # Detect Collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325:
        ball.bounce_x()
    elif ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()

    # Detect when ball goes out of bounds
    # When the Right Paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.score_points_left()

    # When the Left Paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.score_points_right()

screen.exitonclick()
