from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, side):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("square")
        self.setheading(90)
        self.shapesize(stretch_len=5)
        self.create_paddle(side)

    def create_paddle(self, side):
        if side == "right":
            self.setpos(350, 0)
        else:
            self.setpos(-350, 0)

    def move_up(self):
        if self.ycor() < 240:
            self.fd(20)

    def move_down(self):
        if self.ycor() > -240:
            self.bk(20)
