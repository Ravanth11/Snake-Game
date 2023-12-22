from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0,270)
        self.score = 0
        self.update_score()
    

    def update_score(self):
        self.write(f"Score: {self.score}", align = "center",font = ("Arial,24,normal"))

    
    def scoreupdate(self):
        self.score = self.score+1
        self.clear()
        self.update_score()

        

    