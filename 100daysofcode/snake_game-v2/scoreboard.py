from turtle import Turtle
ALIGNMENT = "CENTER"
FONT = (("Courier", 25, "normal"))


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.update_scorebaord()

    def update_scorebaord(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT,
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score = 0
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("game over", align="Center",
    #                font=FONT)

    def scoretrack(self):
        self.score += 1

        self.update_scorebaord()
