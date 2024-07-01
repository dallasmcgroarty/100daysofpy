# scope, local, global, namespace
enemies = 1

def increase_enemies():
  enemies = 2
  print(f"Enemies inside function: {enemies}")

increase_enemies()
print(f"Enemies outside function: {enemies}")  

# local
def drink_potion():
  health += 15
  return

# health is local to the drink_potion() function, so it is 
# not accessible outside
# print(health)

# global
player_health = 10

def drink_potion():
  potion_strength = 2
  player_health *= potion_strength
  return

# player health was defined in the global scope, so it is accessible in
# other functions and anywhere else in the file
print(player_health)


# There is no block scope

if 3 > 2:
  a_variable = 10

game_level = 3
# conditionals don't create their own scope
def create_enemy():
  enemies = ['Skeleton','Zombie','Alien']

  if game_level < 5:
    new_enemy = enemies[0]

  print(new_enemy)


# modifying global scope
enemies = 1

def increase_enemies2():
  # use global variable with global
  # not something you should do often
  global enemies
  enemies += 1
  print(f"enemies inside function: {enemies}")

increase_enemies2()
print(f"enemies outside function: {enemies}")

# better way to use global scope

def increase_enemies_3():
  print(f"enemies inside function: {enemies}")
  return enemies + 1

enemies = increase_enemies_3()
print(f"enemies outside function: {enemies}")


# global constants
# use all uppercase of constants
PI = 3.14159
URL = 'https://google.com'
HANDLE = '@dmcgroarty'