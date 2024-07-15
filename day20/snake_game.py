from turtle import Screen, Turtle
from snake import Snake
import time
import math

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)

segments = []
keys = ['up', 'down', 'right', 'left']

snake = Snake()

screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')

game_on = True
count = 0
while game_on:
  screen.update()
  time.sleep(0.1)

  snake.move()


screen.exitonclick()