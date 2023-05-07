from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color("white") # have to be before the write()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Scores: {self.scores}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.scores += 1
        self.clear() # to make sure the scores won't overlap with each other
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align = ALIGNMENT, font = FONT)
