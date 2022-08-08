import random
from turtle import Turtle


class Dot(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.xposition = random.randint(-280, 280)
        self.yposition = random.randint(-280, 280)
        self.refresh()

    def refresh(self):
        self.xposition = random.randint(-280, 280)
        self.yposition = random.randint(-280, 280)


dot = Dot()
print(dot.xposition, dot.yposition)
print(dot.color)
dot.refresh()
print(dot.xposition, dot.yposition)
