from turtle import Turtle
import random
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("red")
        self.speed("fastest")
        self.refresh()

        
    def refresh(self):
        randomx = random.randint(-200,200)
        randomy = random.randint(-200,200)
        self.goto(randomx,randomy)
    



