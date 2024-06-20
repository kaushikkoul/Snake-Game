from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.teleport(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

    def game_over(self):
        self.teleport(0, 0)
        self.write(f"GAME OVER\nYour score was {self.score}.", align=ALIGNMENT, font=FONT)
