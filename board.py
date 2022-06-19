from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.pencolor("white")
        self.pensize(4)
        self.draw_net()

    def draw_net(self):
        self.penup()
        self.setpos(0, -265)
        self.setheading(90)
        for _ in range(14):
            self.pendown()
            self.fd(20)
            self.penup()
            self.fd(20)



