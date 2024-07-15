class Animal:
  def __init__(self, name):
    self.name = name
    self.eyes = 2

  def breathe(self):
    print('Inhale, exhale')
  
class Fish(Animal):
  def __init__(self):
    super().__init__('Fish')

  def breathe(self):
    super().breathe()
    print('im underwater')

  def swim(self):
    print('moving in water')

nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.name)