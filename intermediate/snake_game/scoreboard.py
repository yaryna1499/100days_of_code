from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.color("black")
        self.penup()
        self.goto(-280, 280)
        self.score = 0
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align='left', font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("Game over!", align='center', font=('Arial', 12, 'normal'))


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

