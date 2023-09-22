from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen=Screen()
screen.bgcolor("black")
screen.title("pong")
screen.setup(width=800,height=600)
screen.tracer(0)

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
scoreboard=Scoreboard()
ball=Ball((0,0))



    
screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    #detect collision with wall
    if ball.ycor()>280 or ball.ycor()<-280 :
        ball.bounce_y()
    #detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<-320 :
        ball.bounce_x()
    #detect collision with right paddle  
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.left_score()
    #detect collision with left paddle  
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.right_score()
        


    

screen.exitonclick()