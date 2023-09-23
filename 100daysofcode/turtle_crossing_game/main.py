import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.title("Tuttle Crossing Game ")
scoreboard=Scoreboard()
player= Player()
cars=CarManager()

screen.onkey(player.move_turtle,"space")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    cars.create_car()
    cars.move_car()
    for car in cars.all_car:
        if player.ycor()>=280:
            player.reset_position()
            scoreboard.increment()
            cars.increase_speed()
    for car in cars.all_car:
        if car.distance(player)<20:
            scoreboard.game_over()
            game_is_on=False

screen.exitonclick()


