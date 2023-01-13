import turtle
from random import randrange

# Draw screen
screen = turtle.Screen()
screen.title('Breakout')
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.tracer(0)

# Draw the edges
edge = turtle.Turtle()
edge.width(10)
edge.goto(300, -400)
edge.left(90)
edge.width(10)
edge.pendown()
edge.pencolor('white')
edge.forward(770)
edge.left(90)
edge.forward(600)
edge.goto(-300, -400)

# Drawing the paddle
paddle = turtle.Turtle()
paddle.goto(0, -220)
paddle.shape('square')
paddle.color('steel blue')
paddle.shapesize(stretch_wid=0.4, stretch_len=2.5)
paddle.penup()

# Drawing the ball
ball = turtle.Turtle()
ball.goto(0, 0)
ball.shape('circle')
ball.color('white')
ball.shapesize(0.4)
ball.penup()
ball.dx = -1
ball.dy = -1


# Draw the hud
def draw_hud(px, py, z):
    hud = turtle.Turtle()
    hud.shape('square')
    hud.color('white')
    hud.penup()
    hud.hideturtle()
    hud.goto(px, py)
    hud.write(f"{z}", align='center', font=("", 30, 'bold'))
    return hud


hud_bricks = draw_hud(-220, 250, "000")
hud_x = draw_hud(-260, 300, "1")
hud_y = draw_hud(140, 250, "000")
hud_ball = draw_hud(100, 300, "1")


# Paddle movements
def paddle_right(paddle):

    x = paddle.xcor()
    if x < 270:
        x += 30
    else:
        x = 270
    return paddle.setx(x)


def paddle_left(paddle):

    x = paddle.xcor()
    if x > -270:
        x -= 30
    else:
        x = -270
    return paddle.setx(x)


# Keyboard for moving the paddle
screen.listen()
screen.onkeypress(lambda: paddle_right(paddle), 'Right')
screen.onkeypress(lambda: paddle_left(paddle), 'Left')

# Building the bricks
blocks_len = []
colors = ['red', 'red', 'orange', 'orange', 'green', 'green', 'yellow', 'yellow']
x_position = []
y_position = []
# Blocks first position
y = 230

for i in range(8):
    y = y - 15
    x = -270
    for j in range(12):
        block = turtle.Turtle()
        block.speed(0)
        block.color(colors[i])
        block.shape('square')
        block.shapesize(stretch_wid=0.5, stretch_len=2.2)
        block.penup()
        block.goto(x, y)
        blocks_len.append(block)
        x_position.append(x)
        y_position.append(y)

        x = x + 49

print(x_position)
print(y_position)
birth_score = 1
score = 0

while True:
    screen.update()

    # Ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Collision with the left wall
    if ball.xcor() == -290:
        ball.dx *= -1

    # Collision with the right wall
    if ball.xcor() == 290:
        ball.dx *= -1

    # Collision with the roof
    if ball.ycor() == 360:
        ball.dy *= -1

    # Collision with the paddle
    if ball.ycor() < -210 and paddle.xcor() + 60 > ball.xcor() > paddle.xcor() - 60:
        ball.dy *= -1

    # Ball 'death'
    if ball.ycor() < -220:
        ball.goto(randrange(-280, 280), 0)
        hud_ball.clear()
        birth_score += 1
        hud_ball = draw_hud(100, 300, f'{birth_score}')

    # Collision with the brick
    def block_hit():
        ball.sety(position_y - 10)
        block.goto(1000, 1000)
        ball.dy *= -1
        blocks_len.remove(block)
        return

    for block in blocks_len:
        position_x = block.xcor()
        position_y = block.ycor()
        if ball.ycor() + 20 == position_y and position_x + 30 > ball.xcor() > position_x - 30:
            block_hit()
            score += 1
            hud_bricks.clear()
            hud_bricks = draw_hud(-220, 250, f'{score}')
            if position_y > 110:
                paddle.shapesize(stretch_wid=0.4, stretch_len=2.3)
            elif position_y > 125:
                paddle.shapesize(stretch_wid=0.4, stretch_len=2.1)
            elif position_y > 140:
                paddle.shapesize(stretch_wid=0.4, stretch_len=1.9)
            elif position_y > 170:
                paddle.shapesize(stretch_wid=0.4, stretch_len=1.7)
            elif position_y > 185:
                paddle.shapesize(stretch_wid=0.4, stretch_len=1.5)
            elif position_y > 200:
                paddle.shapesize(stretch_wid=0.4, stretch_len=1.3)
            elif position_y > 215:
                paddle.shapesize(stretch_wid=0.4, stretch_len=1.1)

        if len(blocks_len) == 0:
            ball.hideturtle()
            hud_game_over = draw_hud(0, 0, "Game is over!")
