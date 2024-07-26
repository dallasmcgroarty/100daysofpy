import pandas
from turtle import Turtle, Screen

screen = Screen()
screen.title('U.S. States Game')
image = 'day25/states_game/blank_states_img.gif'

screen.addshape(image)
main = Turtle()
main.shape(image)

data = pandas.read_csv('day25/states_game/50_states.csv')
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < len(all_states):
  answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct", prompt="What's another state's name?")

  if answer_state == 'exit' or answer_state == None:
    missing_states = []
    for state in all_states:
      if state not in guessed_states:
        missing_states.append(state)
    new_data = pandas.DataFrame(missing_states)
    new_data.to_csv('day25/states_game/states_to_learn.csv')
    break
  else:
    answer_state = answer_state.title()

  if answer_state in all_states:
    state_cords = (data[data.state == answer_state].x.values.tolist()[0],data[data.state == answer_state].y.values.tolist()[0])
    print(state_cords)

    text = Turtle()
    text.penup()
    text.color('black')
    text.ht()
    text.goto(state_cords)
    text.write(answer_state, align='center', font=('Arial', 8, 'normal'))
  
    guessed_states.append(answer_state)

print(missing_states)