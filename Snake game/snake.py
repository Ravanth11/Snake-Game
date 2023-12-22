from turtle import Turtle

class Snake:
    def __init__(self):
        self.segments= []
        self.createsnake()
        
        

    def createsnake(self):
        starting_postions =[(0,0),(-20,0),(-40,0)]
        for i in starting_postions:
            sq1 = Turtle("square")
            sq1.penup()
            sq1.color("white")
            sq1.goto(i)
            self.segments.append(sq1)
   

    def mov(self):
        for segnum in range(2,0,-1):
            newx = self.segments[segnum-1].xcor()
            newy = self.segments[segnum-1].ycor()
            self.segments[segnum].goto(newx,newy)


        self.segments[0].forward(20)
        self.segments[0].speed("fastest")

    def head(self):
        return self.segments[0]

    def up(self):
        self.segments[0].setheading(90)

    def down(self):
        self.segments[0].setheading(-90)

    def right(self):
        self.segments[0].setheading(0)
    def left(self):
        self.segments[0].setheading(-180)

