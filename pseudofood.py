from turtle import Turtle
import random
#was testing another way

class Food():
    def __init__(self):
        self.create_food()


    def create_food(self):
        ball = Turtle()
        ball.shape("circle")
        ball.penup()
        ball.shapesize(stretch_len=0.5, stretch_wid=0.5)
        ball.color("blue")
        ball.speed("fastest")
        self.refresh()

    def refresh(self):
        ball = Turtle()
        ball.goto(x=random.randint(-280,280), y=random.randint(-280,280))


