from turtle import Turtle

FONT = ("Courier", 15, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.ht()
        self.penup()
        self.goto(-220, 265)
        self.pencolor("black")
        self.speed("fastest")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.level} ", False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", False, ALIGNMENT, FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.update_scoreboard()
