# OOP
class Car:
  def __init__(self, make, color):
    self.make = make
    self.color = color

class User:
  def __init__(self, name='', id=None):
    self.name = name
    self.id = id
    self.followers = 0
    self.following = 0

  def follow(self, user):
    self.following += 1
    user.followers += 1


user_1 = User('Dallas','001')
user_2 = User()
print(user_1.name)
print(user_2.id)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)