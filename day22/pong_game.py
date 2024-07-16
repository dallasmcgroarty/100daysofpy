from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('Pong')
screen.tracer(0)

paddleRight = Paddle((350,0))
paddleLeft = Paddle((-350,0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkey(paddleRight.go_up,'Up')
screen.onkey(paddleRight.go_down,'Down')

screen.onkey(paddleLeft.go_up,'w')
screen.onkey(paddleLeft.go_down,'s')
# screen.onkey(snake.left,'Left')
# screen.onkey(snake.right,'Right')

game_on = True

while game_on:
  screen.update()
  ball.move()

  # detect ball hits wall
  if ball.ycor() > 290 or ball.ycor() < -290:
    ball.bounce_y()

  # detect ball hits paddle
  if ball.distance(paddleRight) < 50 and ball.xcor() > 330 or ball.distance(paddleLeft) < 50 and ball.xcor() < -330:
    ball.bounce_x()

  # detect r paddle misses
  if ball.xcor() > 385:
    ball.reset_position()
    score.update_score_left()
  
  # detect r paddle misses
  if ball.xcor() < -385:
    ball.reset_position()
    score.update_score_right()

screen.exitonclick()