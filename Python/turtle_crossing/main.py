import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


##Screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')


##Game_Parts
player = Player() 
score = Scoreboard()
car_manager = CarManager()


##Movement
screen.listen()
screen.onkey(player.move_up,'w')



  

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()


    if player.ycor() > 280 :
        score.scored()
        player.restart()

    car_manager.make_car()
    car_manager.move_forward()

    ##Detect collision
    for car in car_manager.all_cars:
        if player.distance(car) < 18 :
            player.restart()
            score.died()


