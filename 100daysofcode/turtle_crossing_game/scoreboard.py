FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score=1
        self.penup()
        self.color("black")
       
        self.update_scoreboard()
    def update_scoreboard(self):
        self.clear()
        self.goto(-200,250)
        self.write(f"level: {self.score}",align="center",font=("Courier",30,"normal"))
        
    def increment(self):
        self.score+=1
        self.update_scoreboard()
    def game_over(self):
        
        self.goto(0,0)
        self.write("game over",align="center",font=("Courier",50,"normal"))

    
