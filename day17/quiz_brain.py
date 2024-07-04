class Quiz:
  def __init__(self, q_list=[]):
    self.q_number = 0
    self.q_list = q_list

  def next_question(self):
    cur_q = self.q_list[self.q_number]
    self.increment_q_number()

    guess = input(f'Q.{self.q_number}: {cur_q.text} (True/False)?: ')

    return
  
  def still_has_questions(self):
    return self.q_number < len(self.q_list)

  def increment_q_number(self):
    self.q_number += 1

  def ask_question(self):
    pass

  def check_answer(self):
    pass

  def check_end_quiz(self):
    pass