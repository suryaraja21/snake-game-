from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
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