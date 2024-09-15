from turtle import Turtle
import random

# Constants for car color options, starting speed, and speed increment.
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    # Initialize the CarManager class.
    def __init__(self):
        # Create an empty list to store all cars.
        self.all_car = []
        # Set the starting speed for the cars.
        self.car_speed = STARTING_MOVE_DISTANCE
        
    # Method to randomly create a car and add it to the all_car list.
    def create_car(self):
        # Create a car roughly once every 6 times the method is called.
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            # Create a new turtle object to represent the car.
            new_car = Turtle("square")
            # Adjust the shape size of the car.
            new_car.shapesize(1, 2)
            # Set the car's color to a random choice from the COLORS list.
            new_car.color(random.choice(COLORS))
            # Lift the pen to prevent drawing lines.
            new_car.penup()
            # Set the car's direction to left (180 degrees).
            new_car.setheading(180)
            # Place the car at the far right of the screen at a random Y position.
            new_car.goto(300, int(random.randint(-250, 250)))
            # Add the new car to the list of all cars.
            self.all_car.append(new_car)
    
    # Method to move all the cars on the screen.
    def move_car(self):
        for car in self.all_car:
            # Move each car forward by the current speed.
            car.forward(self.car_speed)
    
    # Method to increase the speed of all cars.
    def increase_speed(self):
        # Increase the car speed by a constant value.
        self.car_speed += MOVE_INCREMENT
