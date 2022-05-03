from time import sleep
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('Snake Game')
screen.tracer(0)
 



food = Food()
snake = Snake()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up,'w')
screen.onkey(snake.down,'s')
screen.onkey(snake.left, 'a')
screen.onkey(snake.right, 'd')


game_is_on = True
while game_is_on:
    screen.update()
    sleep(0.1)
    snake.move()

    ### Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        score.update()
        snake.extend()
    
    ## Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < - 280 or snake.head.ycor() > 280 or snake.head.ycor() < -280: 
        score.reset()
        snake.reset()

    ##Detect collision with tail
    for segment in snake.segments_list[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()
    
    
    












screen.exitonclick()