import random
from art import logo
print(logo)


def compare_number(input, actual):
  """Compare the guess with actual number."""
  if input > actual:
    print("Try a smaller number.")
  elif input < actual:
    print("Try a larger number.")
  elif input == actual:
    print("Bingo!")

# make user choose level, easy level gets 10 attempts while diffculty level gets 5.

def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
  if level == 'easy':
    return easy_level
  elif level == 'hard':
    return hard_level
    
easy_level = 10
hard_level = 5
# generate the true number
real_number = random.randint(1,101)

# user instructions
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")




game_continue = True
number_of_games = set_difficulty()
print(f"You have {number_of_games} attempts.")
while game_continue and number_of_games > 0:
  guess = int(input("Make a guess: "))
  compare_number( guess, real_number)
  if guess == real_number:
    game_continue = False
  else:
    number_of_games -=1
    print(f"You have {number_of_games} attempts left.")
    print()

if number_of_games == 0:
  print()
  print(f"Good luck next time! The correct number is {real_number}")
