import random
from turtle import Turtle, Screen

is_race_on = False

screen = Screen()
screen.setup(height = 400, width = 500)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race? Enter a color:")
colors = ['red','purple','green','blue','orange','yellow']
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup() # don't draw the lines
    new_turtle.goto(x = -230, y= y_positions[turtle_index])
    all_turtles.append(new_turtle)


if user_bet: # if user makes their bet, then the game is on!
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230: # if there is a winner
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")
        rand_distance = random.randint(0,10) # make the turtles moves random distance
        turtle.forward(rand_distance)




screen.exitonclick()
