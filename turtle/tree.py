from turtle import *

speed('slowest')

# Turning the turtle to face upwards
rt(-90)

# The acute angle between
# the Y's base and branch
angle = 30


# Function to plot a Y
def plot_y(size, level):

    if level > 0:

        colormode(255)

        # Splitting the rgb range for green
        # into equal intervals for each level
        # Setting the color according
        # to the current level
        pencolor(0, 255//level, 0)

        # Drawing the base
        fd(size)
        rt(angle)

        # Recursive call for the right subtree
        plot_y(0.8 * size, level-1)

        pencolor(0, 255//level, 0)

        lt(2 * angle)

        # Recursive call for the left subtree
        plot_y(0.8 * size, level-1)

        pencolor(0, 255//level, 0)

        rt(angle)
        fd(-size)


plot_y(80, 8)

