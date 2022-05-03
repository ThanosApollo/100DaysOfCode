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
        self.score = n
        with open('snake_game/scores.txt') as data: 
            self.high_score = int(data.read())
            print(self.high_score)
        self.write(f'Score: {str(self.score)}|Highscore: {str(self.high_score)}' ,False,'Center',score_text)
    
    def update(self):
        self.clear()
        self.score += 1
        self.write(f'Score: {str(self.score)}|Highscore: {str(self.high_score)}' ,False,'Center',score_text)

    def reset(self):
        if self.score > self.high_score :
            self.high_score = self.score 
            with open('snake_game/scores.txt', mode='w') as data:   
                data.write(f'{self.high_score}')
        self.score = 0
        self.clear()
        self.write(f'Score: {str(self.score)}|Highscore: {str(self.high_score)}' ,False,'Center',score_text)

        
        
        
    