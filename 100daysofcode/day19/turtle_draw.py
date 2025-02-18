import turtle as t  # Import the turtle module and alias it as 't'

# Create a turtle object
tim = t.Turtle()

# Create a screen object
screen = t.Screen()

# Function to move the turtle forward by 10 units
def move_forward():
    tim.forward(10) 

# Function to turn the turtle left by 90 degrees
def turn_left():
    tim.left(90) 

# Function to turn the turtle right by 90 degrees
def turn_right():
    tim.right(90) 

# Function to move the turtle backward by 10 units
def move_backward():
    tim.backward(10) 

# Listen for keypress events
screen.listen()

# Bind movement functions to specific keys
screen.onkey(key="w", fun=move_forward)  # Move forward when 'w' is pressed
screen.onkey(key="a", fun=turn_left)  # Turn left when 'a' is pressed
screen.onkey(key="d", fun=turn_right)  # Turn right when 'd' is pressed
screen.onkey(key="s", fun=move_backward)  # Move backward when 's' is pressed
screen.onkey(key="space", fun=tim.clear)  # Clear the screen when 'space' is pressed

# Keep the window open until the user clicks
screen.exitonclick()
