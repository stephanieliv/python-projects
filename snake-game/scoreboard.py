from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

with open("data.txt") as data:
    score_record = int(data.read())



class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = score_record
        self.ht()
        self.penup()
        self.goto(0, 265)
        self.pencolor("white")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", False, ALIGNMENT, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def add_points(self):
        self.score += 1
        self.update_scoreboard()
