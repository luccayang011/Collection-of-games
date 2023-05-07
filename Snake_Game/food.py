from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__() # add a super class call, super class is Turtle
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5) # 20 * 0.5 = 10
        self.color("green")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_random = random.randint(-280, 280) # don't want the food to move out of screen. so not strictly the width or length
        y_random = random.randint(-280, 280)
        self.goto(x_random, y_random)
