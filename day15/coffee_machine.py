# coffee maching program
from menu import resources
from menu import MENU

def report():
  for key in resources:
    if key == 'water' or key == 'milk':
      print(F"{key.capitalize()}: {resources[key]}ml")
    elif key == 'coffee':
      print(F"{key.capitalize()}: {resources[key]}g")
    elif key == 'money':
      print(F"{key.capitalize()}: ${resources[key]}")

def calculate_change(item, quarters, dimes, nickels, pennies):
  total = 0
  total += (quarters * 25) / 100
  total += (dimes * 10) / 100
  total += (nickels * 5) / 100
  total += pennies / 100

  if total >= item['cost']:
    change = total - item['cost']
    update_resources(item)
    return change
    
  return None

def update_resources(item):
  resources['money'] += item['cost']
  resources['water'] -= item['ingredients']['water']

  if 'milk' in item:
    resources['milk'] -= item['ingredients']['milk']

  resources['coffee'] -= item['ingredients']['coffee']

  return

def check_resources(item):
  missing = None
  if resources['water'] < item['ingredients']['water']:
    missing = 'water'
  elif 'milk' in item and resources['milk'] < item['ingredients']['milk']:
    missing = 'milk'
  elif resources['coffee'] < item['ingredients']['coffee']:
    missing = 'coffee'

  return missing

def dispense(item):
  return

choice = input("What would you like? (espresso/latte/cappuccino): ")

while choice != 'off':
  if choice == 'report':
    report()
  else:
      item = MENU[choice]

      missing = check_resources(item)
        
      if(missing):
        print(f"Sorry there is not enough {missing}.")
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        continue

      print('Please insert coins.')
      quarters = int(input("How many quarters?: "))
      dimes = int(input("How many dimes?: "))
      nickels = int(input("How many nickels?: "))
      pennies = int(input("How many pennies?: "))

      change = calculate_change(item, quarters, dimes, nickels, pennies)

      if change is not None:
        if change > 0:
          print(f"Here is ${change} in change.")

        print(f"Here is your {choice} ☕, Enjoy!")
      else:
        print(f"You do not have enough money for a {choice}! Money refunded.")

  choice = input("What would you like? (espresso/latte/cappuccino): ")