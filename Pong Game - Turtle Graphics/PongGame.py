import time
from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreBoard import ScoreBoard

screen = Screen()
screen.setup(1000, 600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0) #turn off the animations so we need to update the screen all the time


leftPad = Paddle("left")
rightPad = Paddle("right")
ball = Ball()
score = ScoreBoard()

screen.listen()

screen.onkey(leftPad.up, "w")
screen.onkey(leftPad.down, "s")
screen.onkey(rightPad.up, "Up")
screen.onkey(rightPad.down, "Down")

screen.update()
playing = True

while playing:
    screen.update()
    time.sleep(0.1)

    ball.move()

    # touch up or down borders
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.wallsCollision()
    # touch right or left paddle
    elif (ball.distance(rightPad) < 50 and ball.xcor() > 420) or (ball.distance(leftPad) < 50 and ball.xcor() < -420):
        ball.paddleCollision()
    # touch right border
    elif ball.xcor() > 480:
        score.leftPoint()
        ball.resetPos()
    # touch right border
    elif ball.xcor() < -480:
        score.rightPoint()
        ball.resetPos()
    # game over
    elif score.leftScore == 10 or score.rightScore == 10:
        playing = False

screen.exitonclick()
