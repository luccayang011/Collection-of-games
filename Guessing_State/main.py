import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
states = pd.read_csv("50_states.csv")
guessed_state = []
state_list = states.state.to_list()

while len(guessed_state) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_state)}/50 Guess the state",
                                    prompt="What's the state name?").title()
    if answer_state == 'Exit':
        missing_states = [state for state in state_list if state not in guessed_state] # using list comprehension
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in state_list:
        guessed_state.append(answer_state)
        x = int(states[states.state == answer_state].x)
        y = int(states[states.state == answer_state].y)
        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(x, y)
        state.write(answer_state)

screen.exitonclick()
