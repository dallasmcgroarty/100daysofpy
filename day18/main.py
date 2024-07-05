from turtle import Turtle, Screen
import random
# import everything from turtle module with *
#from turtle import *

#import with alias
#import turtle as t

timmy = Turtle()
timmy.shape('turtle')
timmy.color('red')

screen = Screen()
screen.colormode(255)

# draw a square !!
# for _ in range(4):
#   timmy.forward(100)
#   timmy.right(90)

# draw dashed line !!
# for _ in range(10):
#   timmy.forward(10)
#   timmy.penup()
#   timmy.forward(10)
#   timmy.pendown()

# draw shapes !!
# for sides in range(3, 11):
#   r,g,b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#   timmy.color(r,g,b)
#   angle = 360 / sides
#   for _ in range(0, sides):
#     timmy.forward(100)
#     timmy.right(angle)

# directions = [0, 90, 180, 270]

# timmy.speed(8)
# timmy.pensize(7)
# for _ in range(200):
#   r,g,b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#   timmy.color(r,g,b)
#   timmy.forward(20)
#   timmy.setheading(random.choice(directions))

# python tuples
# tuples can't be changed
my_tuple = (1, 3, 8)
my_tuple[0]

# spirograph !!
# timmy.speed('fastest')
# for i in range(0,365,5):
#   r,g,b = random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)
#   timmy.color(r,g,b)
#   timmy.circle(100)
#   timmy.setheading(i)

screen = Screen()
screen.exitonclick()
