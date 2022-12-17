import turtle
import os

# Draw screen
screen = turtle.Screen()
screen.title("My Pong")
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0)


# Draw paddles one and two
def draw_paddle(x, y):

    paddle = turtle.Turtle()
    paddle.speed(0)
    paddle.shape("square")
    paddle.color("white")
    paddle.shapesize(stretch_wid=5, stretch_len=1)
    paddle.penup()
    paddle.goto(x, y)

    return paddle


paddle_1 = draw_paddle(-350, 0)
paddle_2 = draw_paddle(350, 0)

# Draw ball
ball = turtle.Turtle()
ball.speed(6)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 1
ball.dy = 1

# Defining the initials scores
score_1 = 0
score_2 = 0

# Building head-up display
hud = turtle.Turtle()
hud.speed(0)
hud.shape("square")
hud.color("white")
hud.penup()
hud.hideturtle()
hud.goto(0, 260)
hud.write("0 : 0", align="center", font=("Press Start 2P", 30, "normal"))


# Defining paddles movements
def paddle_up(paddle):

    y = paddle.ycor()
    if y < 250:
        y += 30
    else:
        y = 250
    return paddle.sety(y)


def paddle_down(paddle):

    y = paddle.ycor()
    if y > -250:
        y += -30
    else:
        y = -250
    return paddle.sety(y)


# Keyboard for moving the paddles
screen.listen()
screen.onkeypress(lambda: paddle_up(paddle_1), "w")
screen.onkeypress(lambda: paddle_down(paddle_1), "s")
screen.onkeypress(lambda: paddle_up(paddle_2), "Up")
screen.onkeypress(lambda: paddle_down(paddle_2), "Down")


# Defining a function for the score's update on head-up display
def score_counter():
    hud.clear()
    hud.write("{} : {}".format(score_1, score_2), align="center", font=("Press Start 2P", 24, "normal"))
    ball.goto(0, 0)
    ball.dx *= -1


while True:
    screen.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision with the upper wall
    if ball.ycor() > 290:
        os.system("afplay bounce.wav&")
        ball.sety(290)
        ball.dy *= -1

    # Collision with lower wall
    if ball.ycor() < -290:
        os.system("afplay bounce.wav&")
        ball.sety(-290)
        ball.dy *= -1

    # Collision with left wall
    if ball.xcor() < -355:
        score_2 += 1
        score_counter()

    # Collision with right wall
    if ball.xcor() > 355:
        score_1 += 1
        score_counter()

    # Collision with the paddle 1
    if ball.xcor() < -350 and paddle_1.ycor() + 60 > ball.ycor() > paddle_1.ycor() - 60:
        ball.dx *= -1
        os.system("afplay bounce.wav&")

    # Collision with the paddle 2
    if ball.xcor() > 350 and paddle_2.ycor() + 60 > ball.ycor() > paddle_2.ycor() - 60:
        ball.dx *= -1
        os.system("afplay bounce.wav&")
