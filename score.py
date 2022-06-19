from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.right_score = 0
        self.left_score = 0
        self.penup()
        self.hideturtle()
        self.pensize(4)
        self.pencolor("white")
        self.render_score()

    def render_score(self):
        self.clear()
        self.setpos(60, 245)
        self.pendown()
        self.write(str(self.left_score), align="right", font=('Courier', 40, 'normal'))
        self.penup()
        self.setpos(-60, 245)
        self.write(str(self.right_score), align="left", font=("Courier", 40, 'normal'))
        self.penup()

    def left_scored(self):
        self.left_score += 1
        self.render_score()

    def right_scored(self):
        self.right_score += 1
        self.render_score()

    def game_over(self):
        self.render_score()
        self.setpos(0, 0)
        self.pendown()
        if self.right_score > self.left_score:
            win_text = "Right Side Wins!"
        else:
            win_text = "Left Side Wins!"
        self.write(win_text, align="center", font=("Courier", 30, 'normal'))
