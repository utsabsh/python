from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = (("Courier", 25, "normal"))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scorebaord()

    def update_scorebaord(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("game over", align="Center",
                   font=FONT)

    def scoretrack(self):
        self.score += 1
        self.clear()
        self.update_scorebaord()
