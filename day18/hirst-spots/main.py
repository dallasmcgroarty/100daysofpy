import colorgram
from turtle import Turtle, Screen
import random

timmy = Turtle()

screen = Screen()
screen.colormode(255)

rgb_colors = [(250, 228, 16), (212, 13, 9), (199, 12, 36), (230, 228, 6), (196, 70, 20), (32, 90, 188), (235, 148, 38), (43, 212, 70), (33, 30, 152)]
#colors = colorgram.extract('day18\hirst-spots\spots.png', 12)

# for color in colors:
#   r = color.rgb.r
#   g = color.rgb.g
#   b = color.rgb.b
#   rgb_colors.append((r,g,b))

print(rgb_colors)

# 10 x 10 grid
# 20 dot size
# 50 space between
# timmy.pensize(20)
timmy.hideturtle()
timmy.penup()
timmy.speed('fastest')
timmy.setx(-250)
timmy.sety(-250)

for i in range(0, 10):
  timmy.setx(-250)
  timmy.sety((i * 50) - 250)
  timmy.setheading(0)
  for _ in range(0, 10):
    color = random.choice(rgb_colors)
    timmy.dot(20, color)
    timmy.fd(50)

screen = Screen()
screen.exitonclick()