from turtle import Turtle

POS_LEFT = (-460, 0)
POS_RIGHT = (450, 0)


class Paddle(Turtle):
    def __init__(self, dir):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        if dir == "left":
            self.goto(POS_LEFT)
        elif dir == "right":
            self.goto(POS_RIGHT)

    def up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def down(self):
        self.goto(self.xcor(), self.ycor() - 20)

