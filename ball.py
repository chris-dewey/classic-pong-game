from turtle import Turtle
START_SPEED = 3.5


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.penup()
        self.x_dist = START_SPEED
        self.y_dist = START_SPEED

    def move(self):
        self.goto(self.xcor() + self.x_dist, self.ycor() + self.y_dist)

    def bounce(self):
        self.y_dist *= -1

    def hit(self):
        self.x_dist *= -1
        # Increase ball speed
        self.x_dist *= 1.1
        self.y_dist *= 1.1
        print(f"Ball Speed: {round(abs(self.x_dist), 2)}")

    def restart(self):
        self.setposition(0, 0)
        self.x_dist = START_SPEED
        self.y_dist = START_SPEED
        self.hit()



