from scoreboard import Scoreboard
from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
# screen setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")

screen.title("Snake game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # detect collition with foods
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.scoretrack()
    # detect with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # detect collision with tail
    for segment in snake.segment[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()


# screen exit
screen.exitonclick()
