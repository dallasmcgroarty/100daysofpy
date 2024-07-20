from turtle import Turtle

class Snake:
  def __init__(self):
    self.segments = []
    self.MOVE_DISTANCE = 20
    self.create_snake()
    self.head = self.segments[0]

  def create_segment(self,pos=(0,0)):
    seg = Turtle(shape='square')
    seg.penup()
    seg.color('white')
    seg.goto(pos)
    return seg
  
  def create_snake(self):
    for i in range(0,3):
      x = i * -20
      seg = self.create_segment((x,0))
      self.segments.append(seg)

  def reset(self):
    for seg in self.segments:
      seg.goto(1000, 1000)

    self.segments.clear()
    self.create_snake()
    self.head = self.segments[0]

  def grow(self):
    self.segments.append(self.create_segment(self.segments[-1].position()))
  
  def move(self):
    for i in range(len(self.segments)-1, 0, -1):
      x,y = int(self.segments[i-1].xcor()), int(self.segments[i-1].ycor())
      self.segments[i].goto(x,y)
      #segments[i].seth(heading)

    self.head.fd(self.MOVE_DISTANCE)

  def up(self):
    if self.head.heading() != 270:
      self.head.seth(90)

  def down(self):
    if self.head.heading() != 90:
      self.head.seth(270)

  def left(self):
    if self.head.heading() != 0:
      self.head.seth(180)

  def right(self):
    if self.head.heading() != 180:
      self.head.seth(0)