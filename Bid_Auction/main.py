from replit import clear
from art import logo

print(logo)
bid_finished = False
bids = {}
def find_highest_bidder(bidding_record):
  highest_amount = 0
  for p in bidding_record:
    if bidding_record[p] > highest_amount:
      highest_amount = bidding_record[p]
      winner = p
  print(f"The highest bidder is {winner} with a bid amount of ${highest_amount}.")  
  


while not bid_finished:
  name = input("Please input your name: ")
  bid = int(input("Please input your bid : $"))
  bids[name] = bid
  should_continue = input("Is there any other people want to bid? type 'yes' or 'no'. ").lower()
  if should_continue == "no":
    bid_finished = True
    find_highest_bidder(bids)
  elif should_continue == "yes":
    clear()
