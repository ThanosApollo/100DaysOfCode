from turtle import Turtle

x_pos = 350
y_pos = 0


class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.speed('fastest')
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.goto(position)
        self.up()

    def up(self):
        self.setheading(90)
        self.forward(20)

    def down(self):
        self.setheading(270)
        self.forward(25)