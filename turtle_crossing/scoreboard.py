from time import sleep
from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0,260)
        self.points = 0
        self.write(f'Score:{self.points}',True,'Center',FONT)
    
    def scored(self):
        self.goto(0,260)
        self.clear()
        self.points += 1
        self.write(f'Score:{self.points}',True,'Center',FONT)

    def died(self):
        self.goto(0,260)
        self.clear()
        self.write('You died!',True,'Center',FONT)
        sleep(1)
        self.points = 0
        self.clear()
        self.goto(0,260)
        self.write(f'Score:{self.points}',True,'Center',FONT)