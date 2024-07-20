from turtle import Turtle

class Scoreboard(Turtle):
  def __init__(self):
    super().__init__()
    self.score = 0
    self.high_score = self.get_highscore()
    self.penup()
    self.color('white')
    self.ht()
    self.goto(0, 275)
    self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Arial', 16, 'normal'))

  def update_score(self):
    self.score += 1
    self.refresh() 

  def get_highscore(self):
    with open('day20+21+24/highscore.txt') as file:
      return int(file.read())
  
  def update_highscore(self):
    with open('day20+21+24/highscore.txt', 'w') as file:
        file.write(str(self.high_score))

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      self.update_highscore()

    self.score = 0
    self.refresh()

  # def game_over(self):
  #   self.goto(0, 0)
  #   self.write('GAME OVER', align='center', font=('Arial', 16, 'normal'))

  def refresh(self):
    self.clear()
    self.write(f'Score: {self.score} High Score: {self.high_score}', align='center', font=('Arial', 16, 'normal'))