from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.penup()
    self.color('white')
    self.ht()
    self.goto(0, 275)
    self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal'))

  def update_score(self):
    self.score += 1
    self.refresh()

  def game_over(self):
    self.goto(0, 0)
    self.write('GAME OVER', align='center', font=('Arial', 16, 'normal'))

  def refresh(self):
    self.clear()
    self.write(f'Score: {self.score}', align='center', font=('Arial', 16, 'normal'))