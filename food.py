from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_xcor = random.randint(-280, 280)
        random_ycor = random.randint(-280, 280)
        self.goto(random_xcor, random_ycor)