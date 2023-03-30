import random
from game_data import data
from art import logo, vs
from replit import clear
print(logo)


def compare_followers(A, B):
  """Compare the follower for the two people. Return the one who has more followers."""
  if A['follower_count'] > B['follower_count']:
    return 'A'
  elif A['follower_count'] < B['follower_count']:
    return 'B'
  else:
    return

def personal_info(person):
  info = f"{person['name']}, {person['description']}, from {person['country']}"
  return info


score = 0
game_continue = True
A = random.choice(data)
B = random.choice(data)
while A == B:
  B = random.choice(data)
while game_continue:

  
  print(f"Compare A: {personal_info(A)}")
  print(vs)
  print(f"Against B: {personal_info(B)}")
  
  # let the user choose
  choice = input("Who has more followers? Type 'A' or 'B' ").upper()
  
  # if true, current score + 1, else, end game and output final score
  if choice == compare_followers(A, B):
    score +=1
    print(f"You're right! Current socre: {score}")
    clear()
    A = B
    B = random.choice(data)
    while A == B:
      B = random.choice(data)
  else:
    game_continue = False
    print(f"Sorry, that's wrong. Final score: {score}")
