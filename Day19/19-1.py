from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()


def move_forward():
    timmy.forward(50)

screen.listen()
screen.onkey(key="space", fun=move_forward)









screen.exitonclick()