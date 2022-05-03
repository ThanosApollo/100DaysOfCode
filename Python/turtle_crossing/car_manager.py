import random
from re import X
from shutil import move
from turtle import Turtle


cars = []
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        self.all_cars = []
        super().__init__()
        
    
    def move_forward(self):
        for car in self.all_cars:
            current_x = car.xcor()
            new_x = current_x - 10
            current_y = car.ycor()
            car.goto(new_x,current_y)

    def reset(self):
        current_x = self.xcor()
        new_y = random.randrange(-250,270)
        self.goto(280,new_y)
    
    def make_car(self):
        random_chance = random.randint(1,4)
        if random_chance == 1 :
            new_car = Turtle('square')
            new_car.shapesize(2,1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            new_car.hideturtle
            random_y = random.randrange(-250,250)
            new_car.goto(270,random_y)
            new_car.seth(270)
            self.all_cars.append(new_car)
        
        

 

