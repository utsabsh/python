from turtle import Turtle

class Ball(Turtle):
    def __init__(self, position):
        # Initialize the ball object, inheriting from Turtle class
        super().__init__()
        
        # Set the shape of the ball to "circle"
        self.shape("circle")
        
        # Lift the pen so the ball doesn't leave a trail behind
        self.penup()
        
        # Set the color of the ball to white
        self.color("white")
        
        # Set the initial movement speeds on x and y axes
        self.x_move = 10
        self.y_move = 10
        
        # Set the initial movement speed (affects how fast the ball moves)
        self.move_speed = 0.1
        
    def move(self):
        # Move the ball by the current x and y movement values
        new_x = self.xcor() + self.x_move  # Calculate the new x position
        new_y = self.ycor() + self.y_move  # Calculate the new y position
        self.goto(new_x, new_y)            # Move the ball to the new position
    
    def bounce_y(self):
        # Reverse the ball's direction on the y-axis (bounce vertically)
        self.y_move *= -1
    
    def bounce_x(self):
        # Reverse the ball's direction on the x-axis (bounce horizontally)
        self.x_move *= -1
        
        # Make the ball move faster by decreasing move speed slightly
        self.move_speed *= 0.9
    
    def reset_position(self):
        # Reset the ball's position to the center of the screen
        self.goto(0, 0)
        
        # Reverse the ball's horizontal direction (start moving in the opposite direction)
        self.bounce_x()
        
        # Reset the ball's movement speed back to the original speed
        self.move_speed = 0.1
