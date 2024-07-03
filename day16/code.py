# object oriented programming
# classes and objects
# classes

import another_module

print(another_module.another_variable)

from turtle import Turtle, Screen

timmy = Turtle()
print(timmy)
timmy.shape('turtle')

my_screen = Screen()
print(my_screen.canvheight) # object attribute
my_screen.exitonclick() # object method

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('pokemon name', ['pikachu', 'squirtle','charmander'])
table.add_column('type', ['electric', 'water','fire'])

table.align = 'l'

print(table)