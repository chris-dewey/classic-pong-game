from turtle import Screen
import time
from board import Board
from score import Score
from paddle import Paddle
from ball import Ball


# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Pong!")
screen.bgcolor("black")
screen.tracer(0)

# Game Setup
board = Board()
score = Score()
left_paddle = Paddle("left")
right_paddle = Paddle("right")
ball = Ball()

# Setup Key Listeners & State Machine
keys_pressed = {}


def pressed(event):
    keys_pressed[event.keysym] = True


def released(event):
    keys_pressed[event.keysym] = False


def set_key_binds():
    for key in ["Up", "Down", "w", "s"]:
        screen.getcanvas().bind(f"<KeyPress-{key}>", pressed)
        screen.getcanvas().bind(f"<KeyRelease-{key}>", released)
        keys_pressed[key] = False


def handle_keypress():
    if keys_pressed["w"]:
        left_paddle.move_up()
    if keys_pressed["s"]:
        left_paddle.move_down()
    if keys_pressed["Up"]:
        right_paddle.move_up()
    if keys_pressed["Down"]:
        right_paddle.move_down()


screen.listen()
set_key_binds()

# Main Game
playing = True
while playing:
    time.sleep(0.015)
    handle_keypress()
    screen.update()
    ball.move()

    # Ball Wall Collision Detection
    if ball.ycor() > 285 or ball.ycor() < -285:
        ball.bounce()

    # Ball Paddle Collision Detection
    ball_was_hit = False # Bug fix - edge of paddle causing multiple hits
    if not ball_was_hit:
        if ball.distance(right_paddle) < 55 and ball.xcor() > 330 or ball.distance(left_paddle) < 55 and ball.xcor() < -330:
            ball.hit()
            ball_was_hit = True

    # Score Detection
    if ball.xcor() > 360:
        score.right_scored()
        ball.restart()
    elif ball.xcor() < -360:
        score.left_scored()
        ball.restart()

    # Game Over
    if score.left_score >= 11 or score.right_score >= 11:
        score.game_over()
        playing = False




screen.exitonclick()

