from turtle import Turtle

ALIGN = "center"
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", mode="r") as f:
            high_score = f.readline()
            self.high_score = int(high_score)
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGN, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as f:
                f.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def increase_scoreboard(self):
        self.score += 1
        self.update_scoreboard()
