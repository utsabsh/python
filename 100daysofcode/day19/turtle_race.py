from turtle import Turtle, Screen
import random as r

# Initialize race state
is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

# Prompt the user to place a bet on a turtle color
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Choose your color: ")

# Define turtle colors and their starting positions
colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta'] 
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

# Create six turtle objects and position them at the starting line
for turtle_index in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtles.append(new_turtle)

# Start the race only if the user has placed a bet
if user_bet:
    is_race_on = True

# Race loop
while is_race_on:
    for turtle in all_turtles:
        # Check if a turtle has crossed the finish line
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False  # Stop the race
            
            # Check if the user's bet matches the winning turtle's color
            if winning_color == user_bet:
                print(f"You've Won! The winning color is {winning_color} turtle.")
            else:
                print(f"You've Lost! The winning color is {winning_color} turtle.")

        # Move the turtle forward by a random distance
        rand_distance = r.randint(0, 10)
        turtle.forward(rand_distance)

# Close the screen when clicked
screen.exitonclick()
