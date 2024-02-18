from turtle import Turtle
import random
STARTING=[(0,0),(-20,0),(-40,0)]



class Snake:
    def __init__(self):
        self.segments=[]
        self.createSnake()
        self.head=self.segments[0]
    
    
    def createSnake(self):
        for each in STARTING:
            self.addseg(each)
    def addseg(self,position):
        newseg = Turtle()
        newseg.penup()
        newseg.shape("square")
        newseg.goto(position)
        self.segments.append(newseg)
    def extent(self):
        self.addseg(self.segments[-1].position())
    def moveSnake(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x = self.segments[seg - 1].xcor()
            y = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x, y)
        self.segments[0].forward(20)
    
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



class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("red")
        self.speed("fastest")
        self.randomFood()
    def randomFood(self):
        newx=random.randint(-280,280)
        newy=random.randint(-280,280)
        self.goto(newx,newy)

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.update()
        self.hideturtle()
    def increase(self):
        self.score+=1
        self.clear()
        self.update()
    def update(self):
        self.write(f"Score {self.score}", align='center', font=("Arial", 24, "normal"))
    def over(self):
        self.goto(0,0)
        self.write("Game over", align='center', font=("Arial", 24, "normal"))

        