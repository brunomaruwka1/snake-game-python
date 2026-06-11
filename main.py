from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake by Bruno")

screen.listen()

snake = Snake(4)
food = Food()
scoreboard = Scoreboard()

screen.onkey(key="w", fun=snake.go_up)
screen.onkey(key="a", fun=snake.go_left)
screen.onkey(key="s", fun=snake.go_down)
screen.onkey(key="d", fun=snake.go_right)

count = 0

finished = False
while not finished:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Change color if score == 10
    if scoreboard.score == 5:
        snake.change_color()
        screen.bgcolor("yellow")
        scoreboard.color("black")


    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()
        scoreboard.refresh()

    # Detect collsion with the wall 
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.color("white")
        scoreboard.reset()
        snake.reset()
        screen.bgcolor("black")

    # Detect collision with tail
    for segemnt in snake.segments[1:]:
        if snake.head.distance(segemnt) < 8:
            scoreboard.color("white")
            scoreboard.reset()
            snake.reset()
            screen.bgcolor("black")
            

screen.exitonclick()