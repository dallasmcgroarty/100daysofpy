from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=500)

bet = screen.textinput(title="Make a bet", prompt='Which turtle will win? Enter a color: ')
colors = ['red','orange','yellow','green','blue','purple']
turtles = []
y = -90

def random_move(turtle):
  # race over if 250 or over
  if turtle.xcor() >= 230:
    winning_color = turtle.pencolor()
    
    if winning_color == bet:
      print(f'You won! The {winning_color} turtle won!')
    else:
      print(f'You lost! The {winning_color} turtle won!')
    return False
  
  rand_distance = random.randint(0, 10)
  turtle.fd(rand_distance)
  
  return True

for i in range(len(colors)):
  turtle_y = y + 30
  y = turtle_y
  new_turtle = Turtle(shape='turtle')
  new_turtle.color(colors[i])
  new_turtle.penup()
  new_turtle.goto(-230, turtle_y)
  turtles.append(new_turtle)

if bet:
  race_on = True

while race_on:
  for turtle in turtles:
    race_on = random_move(turtle)
    if not race_on:
      break

screen.exitonclick()