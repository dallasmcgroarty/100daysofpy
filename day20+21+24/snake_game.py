from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
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
food = Food()
scoreboard = Scoreboard()

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

  # collision with food
  if snake.head.distance(food) < 15:
    food.refresh()
    scoreboard.update_score()
    snake.grow()

  # collsion with walls
  if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
      scoreboard.reset()
      snake.reset()

  # detect collision with tail
  for segment in snake.segments[1:]:
    if snake.head.distance(segment) < 10:
      scoreboard.reset()
      snake.reset()


screen.exitonclick()