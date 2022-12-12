import turtle

# Creating the object x,
# so we can use the Turtle functions
a = turtle.Turtle()


def plot_triangle(x, y):

    a.penup()
    a.goto(x, y)
    a.pendown()

    for i in range(3):

        a.forward(100)
        a.left(120)
        a.forward(100)


# Special built on function to send current
# position of cursor to triangle
turtle.onscreenclick(plot_triangle, 1)

# This allows the server to listen to incoming connections
turtle.listen()

turtle.done()
