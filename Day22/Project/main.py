import time
from turtle import Screen

from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Arcade - Pong")
screen.tracer(0)

paddle_l = Paddle((-370, 0))
paddle_r = Paddle((350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=paddle_r.up)
screen.onkey(key="Down", fun=paddle_r.down)
screen.onkey(key="w", fun=paddle_l.up)
screen.onkey(key="s", fun=paddle_l.down)

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()

    # Detect wall and bounce
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce_y()
    # Detect collision with paddle
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -340 and ball.distance(paddle_l) < 50:
        ball.bounce_x()

    # Detect wall collision
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -385:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
