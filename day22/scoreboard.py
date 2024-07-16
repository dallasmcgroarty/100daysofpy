from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.left_score = 0
    self.right_score = 0
    self.penup()
    self.color('white')
    self.ht()
    self.goto(0, 260)
    self.write(f'{self.left_score}      {self.right_score}', align='center', font=('Arial', 20, 'normal'))

  def update_score_left(self):
    self.left_score += 1
    self.refresh()

  def update_score_right(self):
    self.right_score += 1
    self.refresh()

  def game_over(self):
    self.goto(0, 0)
    self.write('GAME OVER', align='center', font=('Arial', 16, 'normal'))

  def refresh(self):
    self.clear()
    self.write(f'{self.left_score}      {self.right_score}', align='center', font=('Arial', 20, 'normal'))