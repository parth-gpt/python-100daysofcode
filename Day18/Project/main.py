# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import turtle
from turtle import Turtle, Screen
import random
color_list = [(245, 243, 238), (247, 242, 244), (240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135), (52, 93, 124), (172, 154, 40), (140, 30, 19), (133, 163, 185), (198, 91, 71), (46, 122, 86), (72, 43, 35), (145, 178, 148), (13, 99, 71), (233, 175, 164), (161, 142, 158), (105, 74, 77), (55, 46, 50), (183, 205, 171), (36, 60, 74), (18, 86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]
timmy = Turtle()
timmy.hideturtle()
turtle.colormode(255)
timmy.speed("fastest")

timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.pendown()

def draw_design(no_of_lines, no_of_dots):
    for line in range(0, no_of_lines):
        for dot in range(0, no_of_dots):
            distance = no_of_dots * 30
            timmy.color()
            timmy.dot(15, random.choice(color_list))
            timmy.penup()
            timmy.forward(30)
            timmy.pendown()
            timmy.dot(15, random.choice(color_list))
        timmy.setheading(90)
        timmy.penup()
        timmy.forward(30)
        timmy.setheading(180)
        timmy.forward(distance)
        timmy.pendown()
        timmy.setheading(0)


draw_design(10, 10)






screen = Screen()
screen.exitonclick()
