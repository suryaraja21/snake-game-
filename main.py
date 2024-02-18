import time
from turtle import Screen
from others import *

snake = Snake()

food = Food()
score = ScoreBoard()
screen = Screen()
screen.setup (width=600, height=600)
screen.tracer(0)
screen.bgcolor("white")

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")

game = True

while game:
    screen.update()
    time.sleep(0.1)
    snake.moveSnake()
    if snake.head.distance(food)<15:
        food.randomFood()
        score.increase()
        snake.extent()
    for seg in snake.segments[1:]:
        if snake.head.distance(seg)<10:
            score.over()
            game=False
    if snake.head.xcor()>290 or snake.head.xcor()<-290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        score.over()
        game=False


screen.exitonclick()
