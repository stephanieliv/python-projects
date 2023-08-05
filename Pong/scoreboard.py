from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 40, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.l_score = 0
        self.r_score = 0
        self.ht()
        self.penup()
        self.pencolor("white")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 240)
        self.write(self.l_score, False, ALIGNMENT, FONT)
        self.goto(100, 240)
        self.write(self.r_score, False, ALIGNMENT, FONT)

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()
