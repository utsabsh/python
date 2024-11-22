from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

# Initialize the game screen
screen = Screen()
screen.bgcolor("black")          # Set background color to black
screen.title("pong")             # Set the window title
screen.setup(width=800, height=600)  # Set screen dimensions
screen.tracer(0)                 # Turn off automatic screen updates for smoother animation

# Create game objects
l_paddle = Paddle((-350, 0))     # Create the left paddle at position (-350, 0)
r_paddle = Paddle((350, 0))      # Create the right paddle at position (350, 0)
scoreboard = Scoreboard()        # Initialize the scoreboard
ball = Ball((0, 0))              # Create the ball at the center of the screen

# Set up key bindings for paddle movement
screen.listen()                  # Listen for keyboard input
screen.onkey(r_paddle.go_up, "Up")       # Move the right paddle up when the "Up" key is pressed
screen.onkey(r_paddle.go_down, "Down")   # Move the right paddle down when the "Down" key is pressed
screen.onkey(l_paddle.go_up, "w")        # Move the left paddle up when "w" is pressed
screen.onkey(l_paddle.go_down, "s")      # Move the left paddle down when "s" is pressed

# Start the game loop
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)  # Control the speed of the game loop
    screen.update()              # Refresh the screen
    ball.move()                  # Move the ball
    
    # Detect collision with the top or bottom walls
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()          # Reverse the ball's vertical direction
    
    # Detect collision with the paddles
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()          # Reverse the ball's horizontal direction

    # Detect when the ball goes out of bounds on the right
    if ball.xcor() > 380:
        ball.reset_position()    # Reset the ball to the center
        scoreboard.left_score()  # Update the left player's score

    # Detect when the ball goes out of bounds on the left
    if ball.xcor() < -380:
        ball.reset_position()    # Reset the ball to the center
        scoreboard.right_score() # Update the right player's score

# Exit the game when the screen is clicked
screen.exitonclick()
