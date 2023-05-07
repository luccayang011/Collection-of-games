from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turn off the tracer

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()  # start listening method to follow the instructions from the keys user has pressed
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()  # refresh screen
    time.sleep(0.1)  # add 0.1second to delay the refresh
    snake.move()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()

    # detect collision with its own tail
    for square in snake.squares[1:]: # skip the head
        if snake.head.distance(square) < 10:
            game_is_on = False
            scoreboard.game_over()



screen.exitonclick()
