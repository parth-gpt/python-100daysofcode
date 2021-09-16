import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.hideturtle()
turtle.colormode(255)


def varColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color

timmy.speed("fastest")


def draw_spirograph(size_of_gap):
    for i in range(int(360/size_of_gap)):
        timmy.color(varColor())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)
        timmy.circle(100)


draw_spirograph(5)



screen = Screen()
screen.exitonclick()