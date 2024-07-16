from turtle import Turtle

class Ball(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.shape('circle')
    self.color('white')
    self.speed('fastest')
    self.goto(0,0)
    self.x_move = 0.06
    self.y_move = 0.05

  def move(self):
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() + self.y_move
    self.goto(new_x, new_y)

  def bounce_y(self):
    self.y_move *= -1

  def bounce_x(self):
    self.x_move *= -1

    # speed up ball
    if self.x_move < 0:
      self.x_move -= .01
    else:
      self.x_move += .01


  def reset_position(self):
    self.x_move = 0.06
    self.goto(0,0)
    self.bounce_x()