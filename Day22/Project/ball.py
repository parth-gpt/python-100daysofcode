from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.createball()
        self.move_x = 0.4
        self.move_y = 0.4

    def createball(self):
        self.shape("circle")
        self.color("white")
        self.penup()

    def move(self):
        new_x = self.xcor() + self.move_x
        new_y = self.ycor() + self.move_y
        self.setpos(x=new_x, y= new_y)

    def bounce_y(self):
        self.move_y *= -1

    def bounce_x(self):
        self.move_x *= -1

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
