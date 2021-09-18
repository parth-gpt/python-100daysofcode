import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)

player = Player()
car_manager = CarManager()
score_board = Scoreboard()

screen.listen()
screen.onkey(key="Up", fun=player.up)

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # Reaching finish line and reseting the player
    if player.ycor() > 280:
        player.res()
        score_board.update_level()
        car_manager.speed()
    car_manager.create_car()
    car_manager.move()

    # Detect car collision with the turtle
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            score_board.game_over()

screen.exitonclick()
