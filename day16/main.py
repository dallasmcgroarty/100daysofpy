from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_handler = MoneyMachine()

items = coffee_menu.get_items()
choice = input(f"What would you like? ({items}): ")

coffee_machine = CoffeeMaker()
coffee_menu = Menu()
money_handler = MoneyMachine()

while choice != 'off':
  if choice == 'report':
    coffee_machine.report()
  else:
    drink = coffee_menu.find_drink(choice)
    if isinstance(drink, MenuItem):
      if coffee_machine.is_resource_sufficient(drink):
        if money_handler.make_payment(drink.cost):
          coffee_machine.make_coffee(drink)

  choice = input(f"What would you like? ({items}): ")
    
