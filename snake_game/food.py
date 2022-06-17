from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        xposition = random.randint(-280, 280)
        yposition = random.randint(-280, 280)
        self.goto(xposition, yposition)

