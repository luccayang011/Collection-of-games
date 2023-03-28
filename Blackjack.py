import random
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_continue = True
# ask user if want to play the game
play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
while game_continue:
  if play_game == 'n':
      game_continue = False
  elif play_game == 'y':
    user_cards = []
    com_cards = []
    card1 = random.choice(cards)
    card2 = random.choice(cards)
    user_cards.append(card1)
    user_cards.append(card2)
    current = card1 + card2
    if current > 21 and 11 in user_cards:
      user_cards[user_cards.index(11)] = 1
    card_com1 = random.choice(cards)
    card_com2 = random.choice(cards)
    com_cards.append(card_com1)
    com_cards.append(card_com2)
    current_com = card_com1 + card_com2
    if current_com > 21 and 11 in com_cards:
      com_cards[com_cards.index(11)] = 1
    # The computer should keep drawing cards unless their score goes over 16.
    while current_com <= 16:
      card_com = random.choice (cards)
      current_com += card_com
      com_cards.append(card_com)
      if current_com > 21 and 11 in com_cards:
        com_cards[com_cards.index(11)] = 1
    print(f"Your cards: {user_cards}. current score: {current}")
    print(f"Computer's first card: {card_com1}")

    new_card = True
    while new_card:
      another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
      # user chose to add new card
      if another_card == 'y':
        card = random.choice(cards)
        user_cards.append(card)
        current += card
        print(f"Your cards: {user_cards}. current score: {current}")
        if current > 21:
          new_card = False
          print(f"Your final hand: {user_cards}, final score: {current}")
          print(f"Computer's final hand: {com_cards}, final score: {current_com}")
          print("You went over. You lose.")
      # user chose not to add new card
      elif another_card == 'n': 
        new_card = False
        # If computer gets blackjack, then the user loses (even if the user also has a blackjack).
        if current_com == 21:
          print(f"Your final hand: {user_cards}, final score: {current}")
          print(f"Computer's final hand: {com_cards}, final score: {current_com}")
          print("You lose.")
        # If the user gets blackjack, user wins.
        elif current == 21:
          print(f"Your final hand: {user_cards}, final score: {current}")
          print(f"Computer's final hand: {com_cards}, final score: {current_com}")
          print("You win.")
        elif current_com > 21:
          print(f"Your final hand: {user_cards}, final score: {current}")
          print(f"Computer's final hand: {com_cards}, final score: {current_com}")
          print("The computer went over, you win.")
          
        # Compare user and computer scores and see if it's a win, loss, or draw.
        elif current_com > current:
          print(f"Your final hand: {user_cards}, final score: {current}")
          print(f"Computer's final hand: {com_cards}, final score: {current_com}")
          print("The computer win.")
        elif current_com == current:
          print(f"Your final hand: {user_cards}, final score: {current}")
          print(f"Computer's final hand: {com_cards}, final score: {current_com}")
          print("Draw.")
        elif current_com < current:
          print(f"Your final hand: {user_cards}, final score: {current}")
          print(f"Computer's final hand: {com_cards}, final score: {current_com}")
          print("You win.")
    # After the game ends, ask the user if they'd like to play again. Clear the console for a fresh start.
    play_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play_game == 'n':
      game_continue = False
    else:
      clear()
    

# Below is Angela's answer #
"""
def deal_card():
  '''Return a random card from the deck.'''
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(card_list):
  '''Take a list of cards and return the score calculated from the cards'''

  if sum(card_list) == 21 and len(card_list) ==2:
    return 0
  if 11 in card_list and sum(card_list):
    card_list.remove(11)
    card_list.append(1)
  return sum(card_list)


def compare(user_score, computer_score):
  if user_score == computer_score:
    return "draw"
  elif computer_score == 0:
    return "lose"
  elif user_score == 0:
    return "win"
  elif user_score > 21:
    return "lose"
  elif computer_score > 21:
    return "win"
  elif user_score > computer_score:
    return "win"
  else:
    return "lose"
    
def play_game():
  user_cards = []
  computer_cards = []
  is_game_over = False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
    
  while not is_game_over:
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
    
    if user_score == 0 or computer_score == 0 or user_score > 21:
      is_game_over = True
    else:
      user_should_deal = input("Another card?")
      if user_should_deal == 'y':
        user_cards.append(deal_card())
      else:
        is_game_over = True
 
      
  while computer_score != 0 and computer_score < 17:
    computer_cards.append(deal_card())
    computer_score = calculate_score(computer_cards)
  
  print(compare(user_score, computer_score))
  
while input("continue?") == 'y':
  clear()
  play_game()

"""
