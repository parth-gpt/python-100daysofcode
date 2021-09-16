from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.back(10)


def rotate_clockwise():
    timmy.right(10)


def rotate_counter():
    timmy.left(10)


def clear():
    timmy.reset()

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="d", fun=rotate_clockwise)
screen.onkey(key="a", fun=rotate_counter)
screen.onkey(key="c", fun=clear)





screen.exitonclick()