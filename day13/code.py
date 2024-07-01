# debugging, find and fix errors

############DEBUGGING#####################

# # Describe Problem
def my_function():
  for i in range(1, 20): #1, 21 to fix
    if i == 20:
      print("You got it")
my_function()

# problem here is we are checking if i == 20, but the range is exlusive on the end,
# so we never hit 20, the end range needs to be 21

# # Reproduce the Bug
from random import randint
dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(1, 6) # 0, 5 to fix
print(dice_imgs[dice_num])

# bug here is the dice_imgs list is 0 - 5 indexed, but the dice_num randint is 
# choosing numbers from 1 - 6, so 0 is never chosen and 6 returns an index error

# # Play Computer
year = int(input("What's your year of birth?"))
if year > 1980 and year < 1994:
  print("You are a millenial.")
elif year > 1994: # >= to fix
  print("You are a Gen Z.")

# entering 1994 is fale on both conditions, so it doesn't print anything
# need to add a <= or >= to catch the 1994 case

# # Fix the Errors
age = int(input("How old are you?")) # int(input)
if age > 18:
  print(f"You can drive at age {age}.") # indent to fix, add f string as well

# print statement is not indented, indent the line or add a new line of code
# under the condition statement that is also indented
# the input also needs to be cast to an int
# also add f string to print

# #Print is Your Friend
pages = 0
word_per_page = 0
pages = int(input("Number of pages: "))
word_per_page = int(input("Number of words per page: ")) # change == to =
total_words = pages * word_per_page
print(total_words)

# error here is word_per_page is being compared with == and not being assigned
# use = to fix

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item) # indent to be in for loop
  print(b_list)

mutate([1,2,3,5,8,13])

# issue here is we are only appending the last item to the b_list
# move the b_list.append(new_item under in for loop) to fix