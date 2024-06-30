############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##########################################

from art import logo
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

user_cards = []
computer_cards = []

# deal random card from deck
def deal_card():
  return random.choice(cards)

# compare computer and user hands
def compare(user_cards, computer_cards):
  win = False
  draw = False
  user_total = sum(user_cards)
  computer_total = sum(computer_cards)

  if computer_total > 21:
    win = True
  elif (user_total == 21 and len(user_cards) == 2) and (computer_total == 21 and len(computer_cards) == 2):
    draw = True
  elif user_total == 21 and len(user_cards) == 2:
    win = True
  elif computer_total == 21 and len(computer_cards) == 2:
    win = False
  elif user_total > computer_total:
    win = True
  elif user_total < computer_total:
    win = False
  else:
    draw = True

  print(f"Your final hand: {user_cards}")
  print(f"Computer's final hand: {computer_cards}")
  
  if draw:
    print('It\'s a draw!')
  elif win:
    print('You win!')
  else:
    print('You lose!')

# deal the computer out
def deal_out_computer():
  computer_total = sum(computer_cards)

  while computer_total < 17:
    computer_cards.append(deal_card())

    if computer_total > 21:
      if 11 in computer_cards:
        computer_cards.remove(11)
        computer_cards.append(1)

    computer_total = sum(computer_cards)
    
  return

play = input('Do you want to play a game of Blackjack? Type \'y\' or \'no\': ')

while play == 'y':
  # clear out hands
  user_cards.clear()
  computer_cards.clear()

  # print nice logo
  print(logo)

  # deal user two cards
  user_cards.append(deal_card())
  user_cards.append(deal_card())

  print(f'Your cards: {user_cards}')

  # deal computer two cards
  computer_cards.append(deal_card())
  computer_cards.append(deal_card())

  print(f'Computer\'s first card: {computer_cards[0]}')

  deal_user = input(f"Type 'y' to get another card, type 'n' to pass: ")

  bust = False

  # deal cards while user wants
  while deal_user == 'y':
    user_cards.append(deal_card())

    user_total = sum(user_cards)

    # handle busting
    if user_total > 21:
      if 11 in user_cards:
        user_cards.remove(11)
        user_cards.append(1)
      else:
        bust = True
        break

    #display cards
    print(f"Your cards: {user_cards}")
    print(f"Computer's first card: {computer_cards[0]}")

    # get input again if not busted yet
    deal_user = input(f"Type 'y' to get another card, type 'n' to pass: ")

  # if bust display hand and lose
  if bust:
    print(f"Your final hand: {user_cards}")
    print('You bust! You lose!')
  else:
    # no bust, user stopped dealing, deal out computer and compare
    deal_out_computer()
    compare(user_cards, computer_cards)

  # play again?
  play = input('Do you want to play a game of Blackjack? Type \'y\' or \'no\': ')
