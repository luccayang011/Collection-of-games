from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.levels = 1
        self.color("black")
        self.penup()
        self.goto(-270, 260)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.levels}", align="left", font=FONT)

    def increase_score(self):
        self.levels += 1
        self.clear() # clear the previous scores
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = "center", font = FONT)
