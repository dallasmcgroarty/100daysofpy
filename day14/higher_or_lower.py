# higher or lower game
from art import logo
from art import vs
from game_data import data
import random

def compare(A, B, choice):
  if A['follower_count'] > B['follower_count'] and choice == 'a':
    return True
  elif A['follower_count'] < B['follower_count'] and choice == 'a':
    return False
  elif B['follower_count'] > A['follower_count'] and choice == 'b':
    return True
  else:
    return False


def remove_item(name):
  for item in data:
    if name == item['name']:
      data.remove(item)


score = 0
correct = True

compareA = random.choice(data)
compareB = random.choice(data)

if compareB['name'] == compareA['name']:
  compareB = random.choice(data)

while correct:
  print(logo)
  if score > 0:
    print(f"Your're right! Current score: {score}")

  print(f"Compare A: {compareA['name']}, a {compareA['description']}, from {compareA['country']}")

  print(vs)
  print(f"Compare B: {compareB['name']}, a {compareB['description']}, from {compareB['country']}")

  choice = input('Who has more followers? Type \'A\' or \'B\': ').lower()

  correct = compare(compareA, compareB, choice)

  if correct:
    score += 1
    compareA = compareB

    if compareB['name'] == compareA['name']:
      compareB = random.choice(data)

print(logo)
print(f"Sorry, that's wrong. Final score: {score}")