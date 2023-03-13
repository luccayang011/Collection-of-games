#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ''
for letter in range(0,nr_letters):
  password = password + letters[random.randint(0,len(letters)-1)]
  # or use:
  # password += random.choice(letters)

for symbol in range(0,nr_symbols):
  password = password + symbols[random.randint(0,len(symbols)-1)]
  # or use:
  # password += random.choice(symbols)
  
for number in range(0,nr_numbers):
  password = password + numbers[random.randint(0,len(numbers)-1)]

  # or use:
  # password += random.choice(numbers)
  
print(password)

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

#Solution 1: my own solution
password = ''
for letter in range(0,nr_letters):
  password = password + letters[random.randint(0,len(letters)-1)]
  # or use:
  # password += random.choice(letters)
  
for symbol in range(0,nr_symbols):
  password = password + symbols[random.randint(0,len(symbols)-1)]
  # or use:
  # password += random.choice(symbols)
  
for number in range(0,nr_numbers):
  password = password + numbers[random.randint(0,len(numbers)-1)]
  # or use:
  # password += random.choice(numbers)

password_random = ''
for i in range(0,len(password)):
  random_char_index = random.randint(0,len(password)-1)
  random_char = password[random_char_index]
  password_random = password_random + random_char
  password = password[:random_char_index] + password[random_char_index+1:]

print(password_random)


#Solution 2:from Angela
password_list = []
for letter in range(0,nr_letters):
  password_list.append(random.choice(letters))
  
for symbol in range(0,nr_symbols):
  password_list.append(random.choice(symbols))
  
for number in range(0,nr_numbers):
  password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ''
for char in password_list:
  password += char

print(f"you password is: {password}")

#code challenge from 100 Days of Code: The Complete Python Pro Bootcamp for 2023

