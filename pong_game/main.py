from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from time import sleep
from scoreboard import Score

## Screen 
screen = Screen()
screen.bgcolor('black')
screen.setup(800,600)
screen.title('Pong Game')
screen.tracer(0)




### Components
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
score = Score()



### Movement
screen.listen()
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')


game_is_on = True
while game_is_on :
    ball.move()
    sleep(0.05)
    screen.update()

    if ball.ycor() > 280 or ball.ycor() < -280 :
        ball.bounce_y()
    
    ##Collision with paddle
    if ball.distance(r_paddle) < 60 and ball.xcor() > 320 or ball.distance(l_paddle) < 60 and ball.xcor() < -320:
        ball.bounce_x()

    ## Reset and give point
    #Right
    if ball.xcor() > 370:
        ball.reset()
        score.right_point()
    #Left
    if ball.xcor() < -370:
        ball.reset()
        score.left_point()
        





































