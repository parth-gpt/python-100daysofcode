import turtle
import pandas
from turtle import Screen, Turtle

screen = Screen()
screen.title("U.S. States Game")
screen.setup(width=725, height=491)
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
data_list = data.state.tolist()
guessed_state = []
states = 0
while states <= 50:
    answer_state = screen.textinput(title=f"{states}/50 States Guessed", prompt="Guess another state?").title()

    if answer_state == "Exit":
        missing_states = []
        for state in data_list:
            if state not in guessed_state:
                missing_states.append(state)
        data = pandas.DataFrame(missing_states)
        data.to_csv("states_to_learn.csv")
        break
    if answer_state in data_list:
        guessed_state.append(answer_state)
        answer = data[data.state == answer_state]
        pen = Turtle()
        pen.hideturtle()
        pen.penup()
        pen.goto(x=int(answer.x), y=int(answer.y))
        pen.pendown()
        pen.write(answer_state,
                  font=("Arial", 10, "normal"))  # answer.state.item() can also be used instaed of answer_state.title()
        states += 1
