from question_model import Question
from data import question_data
from quiz_brain import Quiz

question_bank = []

for q in question_data:
  question_bank.append(Question(q['text'], q['answer']))

quiz = Quiz(question_bank)
quiz.next_question()

while quiz.still_has_questions():
  quiz.next_question()

quiz.final_score()