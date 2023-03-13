import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors.\n"))
computer = random.randint(0,2)
rps_list = [rock,paper,scissors]

if user > 2 or user < 0:
  print("You typed an invalid number, you lose.")
else:
  print("You:")
  print(rps_list[user])
  print("Computer:")
  print(rps_list[computer])


if user == 0:
  if computer == 0:
    print("Tie!")
  elif computer == 1:
    print("You lose.")
  else:
    print("You win!")


if user == 1:
  if computer == 0:
    print("You win!")
  elif computer == 1:
    print("Tie!")
  else:
    print("You lose.")

if user == 2:
  if computer == 0:
    print("You lose.")
  elif computer == 1:
    print("You win!")
  else:
    print("Tie!")
    
 # it's a coding exercise from 100 Days of Code: The Complete Python Pro Bootcamp for 2023
