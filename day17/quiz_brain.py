class Quiz:
  def __init__(self, q_list=[]):
    self.q_number = 0
    self.score = 0
    self.q_list = q_list

  def next_question(self):
    cur_q = self.q_list[self.q_number]
    self.increment_q_number()

    guess = input(f'Q.{self.q_number}: {cur_q.text} (True/False)?: ').lower()

    if self.check_answer(guess, cur_q.answer):
      print('You got it right!')
      self.increment_score()
    else:
      print("That's wrong.")

    print(f"The correct answer was: {cur_q.answer}")
    print(f"Your current score is: {self.score}/{self.q_number}")
    print()

    return
  
  def still_has_questions(self):
    return self.q_number < len(self.q_list)

  def increment_q_number(self):
    self.q_number += 1

  def increment_score(self):
    self.score += 1

  def final_score(self):
    print('You\'ve completed the quiz!')
    print(f'Your final score was: {self.score}/{len(self.q_list)}')

  def check_answer(self, guess, answer):
    return guess == answer.lower()
  