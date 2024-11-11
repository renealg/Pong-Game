from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=0.8, stretch_wid=0.8)
        self.moveX = 10
        self.moveY = 10

    def move(self):
        self.goto(self.xcor() + self.moveX, self.ycor() + self.moveY)

    def wallsCollision(self):
        self.moveY *= -1

    def paddleCollision(self):
        self.moveX *= -1

    def resetPos(self):
        self.goto(0, 0)
        self.moveX *= random.randrange(-1, 2, 2)
        self.moveY *= random.randrange(-1, 2, 2)