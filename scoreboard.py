from turtle import Turtle

FONT = ("Courier", 20, "normal")
ALIGNMENT = "center"

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.style = ("Courier", 15, "normal")
        self.goto(0, 270)
        self.write(f"Score: {self.score}", font=FONT, align=ALIGNMENT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.goto(0, 270)
        self.write(f"Score: {self.score}", True, font=self.style, align="center")

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", font=FONT, align=ALIGNMENT)

