from turtle import Turtle,Screen
import random as r

is_race_on=False
screen=Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle wiil win the race? choose your color: ")

colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta'] 
y_position=[-70,-40,-10,20,50,80 ]
all_turtle=[]

    
for turtle_index in range(0,6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x=-230,y=y_position[turtle_index])
    new_turtle.color(colors[turtle_index])
    all_turtle.append(new_turtle)

if user_bet:
    is_race_on=True

while is_race_on:
    
    for turtle in all_turtle:
        if turtle.xcor()>230:
            winning_color=turtle.pencolor()
            is_race_on=False
            if winning_color==user_bet:
                print(f"you've Won! The winning color is {winning_color} turtle")
            else:
                print(f"you've Lost! The winning color is {winning_color} turtle")
        rand_distance = r.randint(0,10)
        turtle.forward(rand_distance)



screen.exitonclick()