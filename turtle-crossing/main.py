from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    car.create_car()
    car.move_car()

    for cars in car.all_cars:
        if cars.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.goto(0, -280)
        scoreboard.increase_level()
        car.level_up()











screen.exitonclick()
