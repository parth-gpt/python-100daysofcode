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


def draw():
    for i in range(3,11):
        timmy.color(varColor())
        angle = 360/i
        for j in range(0, i):
            timmy.forward(100)
            timmy.right(angle)
    timmy.forward(100)



draw()












screen = Screen()
screen.exitonclick()