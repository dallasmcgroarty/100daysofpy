COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

import random
from turtle import Turtle

class CarManager:
    def __init__(self):
        self.cars = []
        self.speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        
        if random_chance == 1:
            new_car = Turtle('square')
            new_car.penup()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.speed('fast')
            new_car.goto(320, self.get_random_y())
            self.cars.append(new_car)

    def get_random_y(self):
        return random.randint(-250, 280)
    
    def move_cars(self):
        for car in self.cars:
            car.bk(self.speed)

    def clear_cars(self):
        for car in self.cars:
            car.hideturtle()
            self.cars.remove(car)

    def increment_speed(self):
        self.speed += MOVE_INCREMENT

    def level_up(self):
        self.clear_cars()
        self.increment_speed()