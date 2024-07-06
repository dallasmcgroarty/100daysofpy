from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
  tim.fd(5)

def move_backwards():
  tim.bk(5)

def move_counter_clockwise():
  cur_heading = tim.heading()

  if cur_heading == 0:
    cur_heading = 360

  cur_heading -= 5

  tim.setheading(cur_heading)

def move_clockwise():
  cur_heading = tim.heading()

  if cur_heading == 360:
    cur_heading = 0

  cur_heading += 5

  tim.setheading(cur_heading)

def clear():
  tim.reset()

# clear screen on c
screen.onkey(key='c', fun=clear)

# move forward on w
screen.onkeypress(key='w', fun=move_forwards)

# move counter-clockwise on a
screen.onkeypress(key='a', fun=move_counter_clockwise)

# move clockwise on d
screen.onkeypress(key='d', fun=move_clockwise)

# move backwards on s
screen.onkeypress(key='s', fun=move_backwards)

screen.listen()
screen.exitonclick()

# higher order functions
# functions that use accept functions as inputs/works with other functions