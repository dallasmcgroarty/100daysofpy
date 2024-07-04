class Question:
  def __init__(self, text='', answer=''):
    self.text = text
    self.answer = answer

  def __str__(self) -> str:
    return f"The text is {self.text} and the answer is {self.answer}"