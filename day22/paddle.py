from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()
    self.position = position
    self.penup()
    self.shape('square')
    self.shapesize(stretch_wid=5, stretch_len=1)
    self.color('white')
    self.speed('fast')
    self.goto(self.position)

  def go_up(self):
    new_y = self.ycor() + 25
    if self.check_height_top():
      self.goto(self.xcor(), new_y)

  def go_down(self):
    new_y = self.ycor() - 25
    if self.check_height_bottom():
      self.goto(self.xcor(), new_y)

  def check_height_top(self):
    if self.ycor() >= 250:
      return False
    else:
      return True

  def check_height_bottom(self):
    if self.ycor() <= -250:
      return False
    else:
      return True