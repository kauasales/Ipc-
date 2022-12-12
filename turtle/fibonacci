# Plotting Fibonacci
# spiral fractal using Turtle
import math
import turtle


def plotting_fibonacci(elements):

    constant0 = 0
    constant1 = 1
    square0 = constant0
    square1 = constant1

    # Defining the plotting pen to blue
    x.pencolor("green")

    # Drawing the first square
    # We don't need a square for the element zero,
    # so we start with the element one
    x.forward(constant1 * factor)
    x.left(90)
    x.forward(constant1 * factor)
    x.left(90)
    x.forward(constant1 * factor)
    x.left(90)
    x.forward(constant1 * factor)

    # Proceeding with the Fibonacci Series
    temp = square1
    square1 = square1 + square0
    square0 = temp

    # Drawing the rest og the squares
    for i in range(1, elements):

        x.backward(square0 * factor)
        x.right(90)
        x.forward(square1 * factor)
        x.left(90)
        x.forward(square1 * factor)
        x.left(90)
        x.forward(square1 * factor)

        # Proceeding with the Fibonacci Series
        temp = square1
        square1 = square1 + square0
        square0 = temp

    # Bringing the pen, so we can start pointing the spiral
    x.penup()
    x.goto(factor, 0)
    x.seth(0)
    x.pendown()

    # Defining the plotting pen to yellow
    x.pencolor("yellow")

    # Fibonacci Spiral Plot
    x.left(90)

    for i in range(elements):

        print(constant1)
        spiral_formula = math.pi * constant1 * factor / 2
        spiral_formula /= 90

        for j in range(90):

            x.forward(spiral_formula)
            x.left(1)
        temp = constant0
        constant0 = constant1
        constant1 = temp + constant1


# Here 'factor' signifies the multiplicative
# factor which expands or shrinks the scale
# of the plot by a certain factor.
factor = 1

# Creating an input for our "n" elements
elements = int(input("Enter the number of iterations (must be > 1): "))

# Plotting the Fibonacci Spiral Fractal
# and printing the corresponding Fibonacci Number

if elements > 0:

    print("Fibonacci series for", elements, "elements: ")
    x = turtle.Turtle()
    x.speed(100)
    x.shape("turtle")
    x.color("blue")
    plotting_fibonacci(elements)
    turtle.done()

else:

    print("Iterations number must be > 0")
