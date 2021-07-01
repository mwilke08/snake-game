from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.style = ("Courier", 15, "normal")
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score} High Score: {self.high_score}", True, font=self.style, align="center")

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as file:
                score_to_write = f"{self.score}"
                file.write(score_to_write)
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()


