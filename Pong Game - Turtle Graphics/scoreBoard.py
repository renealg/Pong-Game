from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.leftScore = 0
        self.rightScore = 0
        self.changeScore()

    def changeScore(self):
        self.goto(-100, 220)
        self.write(self.leftScore, align="center", font=("Courier", 50, "normal"))
        self.goto(100, 220)
        self.write(self.rightScore, align="center", font=("Courier", 50, "normal"))

    def leftPoint(self):
        self.leftScore += 1
        self.clear()
        self.changeScore()

    def rightPoint(self):
        self.rightScore += 1
        self.clear()
        self.changeScore()
