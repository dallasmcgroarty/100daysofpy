import random
from art import logo

answer = 0

def play():
  global answer
  answer = random.randint(1, 100)

  print(logo)
  print('Welcome to the Number Guessing Game!')
  print("I'm thinking of a number between 1 and 100.")
  print(f"Pssst, the correct answer is {answer}")

  difficulty = input(f"Choose a difficulty. Type 'easy' or 'hard': ")

  if difficulty != 'easy' and difficulty != 'hard':
    print("Please enter only 'easy' or 'hard'")
    exit()
  elif difficulty == 'easy':
    guesses = 10
  elif difficulty == 'hard':
    guesses = 5

  return start_game_loop(answer, guesses)

def start_game_loop(answer, guesses):
  while guesses > 0:
    print(f"You have {guesses} attempts remaining to guess the number.")

    guess = input("Make a guess: ")

    while not guess.isdigit():
      print('Please only enter numbers.')
      guess = input("Make a guess: ")

    guess = int(guess)

    if guess == answer:
      return True
    elif guess < answer:
      print('Too low.\nGuess again.')
    elif guess > answer:
      print('Too high.\nGuess again.')
    
    guesses -= 1
  
  return False

win = play()

if not win:
  print('You ran out of guesses, you lose.')
else:
  print(f"You got it! The answer is {answer}.")