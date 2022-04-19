from turtle import Turtle, goto

position = (0,270)
n = 0
score_text = ('Courier', 20, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(position)
        self.color('white')
        self.hideturtle()
        self.n = n
        self.write(f'Score: {str(self.n)}' ,False,'Center',score_text)
    
    def update(self):
        self.clear()
        self.n += 1
        self.write(f'Score: {str(self.n)}' ,False,'Center',score_text)

    def game_over(self): 
        self.goto(0,0)
        self.write("GAME OVER", False, 'Center', score_text)
        
        
        
    