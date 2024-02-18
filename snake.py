from turtle import Turtle
START=[(0,0),(-20,0),(-40,0)]

class Snake:
    def __init__(self):
        self.segment=[]
        self.createsnake()
        self.head=self.segment[0]
    
    def move(self):
        for seg in range(len(self.segment)-1,0,-1):
            new_x=self.segment[seg-1].xcor()
            new_y=self.segment[seg-1].ycor()
            self.segment[seg].goto(new_x,new_y)
        self.segment[0].forward(20)
    
    def createsnake(self):
        for position in START:
            self.addseg(position)
    def grow(self):
        self.addseg(self.segment[-1].position())

    def addseg(self,position):
        new_segments = Turtle()
        new_segments.shape("square")
        new_segments.color("white")
        new_segments.penup()
        self.segment.append(new_segments)
        new_segments.goto(position)


    def up(self):
        if self.head.heading()!=270:
            self.head.setheading(90)
    def down(self):
        if self.head.heading()!=90:
            self.head.setheading(270)
    def right(self):
        if self.head.heading()!=180:
            self.head.setheading(0)
    def left(self):
        if self.head.heading()!=0:
            self.head.setheading(180)