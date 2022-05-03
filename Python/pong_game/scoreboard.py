from turtle import Turtle

from pygame import init

text_font = ('Courier', 20, 'normal')
score_left = 0
score_right = 0

class Score(Turtle): 
    def __init__(self):
        super().__init__()    
        self.goto(x=0,y=250) 
        self.hideturtle()
        self.penup()
        self.color('white')
        self.score_left = score_left
        self.score_right = score_right
        self.write(f'{str(self.score_left)} | {str(self.score_right)}', True, 'center', text_font)

    def right_point(self) : 
        self.clear()
        self.score_right += 1
        self.goto(0,250)
        self.write(f'{str(self.score_left)} | {str(self.score_right)}', True, 'center', text_font)
    
    def left_point(self): 
        self.clear()
        self.score_left += 1
        self.goto(0,250)
        self.write(f'{str(self.score_left)} | {str(self.score_right)}', True, 'center', text_font)
    
