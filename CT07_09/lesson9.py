

# Import libraries
import turtle
import time
import random
import math


#global variables
screen=turtle.Screen()
t = turtle.Turtle()
# fuctions

def sq(size):  #draw square
    t.seth(0)
    t.pendown()
    for i in range(4):
        t.forward(size)
        t.right(90)
    t.penup()
def done():
    turtle.done()
def f(length):
    t.forward(length)
def r(degree):
    t.right(degree)
def l(degree):
    t.forward(degree)

def polygon(length,sides):
    t.seth(0)
    t.pendown()
    for i in range(sides):
        t.forward(length)
        t.right(360/sides)
    t.penup()


# main code
t.pu()
t.speed(0)
t.goto(0,0)

t.pd()







# done()

# ## Task 2: Square in a Square
# Use a function with parameters to draw 7 squares inside each other, getting smaller and smaller.

# 1. Import the ‘turtle’ library
# 2. Create a 400x400 screen
# 3. Create a function “draw_square” with a “size” parameter
# 4. The “draw_square” function will draw a square of size*size around the (0,0) coordinate.
# 5. Within a ‘for’ loop, use the “draw_square” function you have created to draw 7 squares around the (0,0) coordinate with the following sizes: 50, 100, 150, 200, 250, 300, 350
# t.seth(0)
# size = 350
# for i in range(7):
#     t.penup()
#     t.goto(-size/2,size/2)
#     t.pendown()
#     sq(size)
#     size = size - 50

# turtle.done()

# ## Task 3: Shape Creator
# You want to create a shape creator program that will draw any shape you want simply by giving the program the length and number of sides that the shape must have.

# To do this, you need to create a function with 2 parameters:
# - ‘length’
# - ‘num_sides’

# 1. Create a function called draw_shape() that takes in the length of the sides, as well as the number of sides.
# 2. The function should draw a shape with the length of sides and number of sides given by calculating the exterior angle
# 3. Using the  draw_shape() function, draw the following:
# - Pentagon, Hexagon, Octagon and Decagon


# length = int(screen.textinput("length","Enter length: "))
# sides = int(screen.textinput("sides", "enter sides: "))
# polygon(length,sides)

# modify the functions such that the perimeter is the same

# def polygonsame(perimeter,sides):
#     t.seth(0)
#     t.pendown()
#     length = perimeter / sides
#     for i in range(sides):
#         t.forward(length)
#         t.right(360/sides)
#     t.penup()

# perimeter = int(screen.textinput("Perimeter","Enter perimeter: "))
# sides = int(screen.textinput("sides", "enter sides: "))
# polygonsame(perimeter,sides)


# ## Task 4: Drawing a House
# You have been tasked to draw a house (made of a square and a triangle)

# Using the ‘draw_shape’ function you have just created, create a house by first drawing a square, then a triangle above the square.
# 1. The house is made up of a 100x100 square and a triangle that is 100 units long each side.
# 2. The triangle must be connected to the square

# You may refer to the following as a guide:
# 1. Import ‘turtle’ library
# 2. Set up a window
# 3. Create a turtle object and lift the pen to move without drawing
# 4. Define ‘draw_shape’ function to draw a regular polygon based on specified length and number of sides
# 5. Define ‘draw_house’ function that uses the ‘draw_shape’ function to combine a square and a triangle

def draw_shape(length,sides):
    t.seth(0)
    t.pendown()
    for i in range(sides):
        t.forward(length)
        t.left(360/sides)
    t.penup()

def draw_house(x,y):
    t.penup()
    t.goto(x,y)
    t.pendown()
    draw_shape(100,4)
    t.goto(x,y+100)
    draw_shape(100,3)
    # t.seth(180)
    # t.forward(100)
    # t.seth(60)
    # t.forward(100)
    # t.seth(-60)
    # t.forward(100)
    # t.seth(180)
    # t.forward(100)
    # t.seth(0)
    # sq(100)
draw_house(20,50)

turtle.done()