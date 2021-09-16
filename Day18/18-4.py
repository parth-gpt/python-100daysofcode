import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
turtle.colormode(255)


def varColor():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


direct_angles = [0, 90, 180, 270]
timmy.pensize(15)
timmy.speed("fastest")
for i in range(0, 400):
    timmy.color(varColor())
    timmy.forward(30)
    timmy.setheading(random.choice(direct_angles))

screen = Screen()
screen.exitonclick()
