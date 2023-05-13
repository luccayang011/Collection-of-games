import pandas as pd


nato_data = pd.read_csv('nato_phonetic_alphabet.csv')
nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}

user_input = input("Please input your word: ").upper()
result = [nato_dict[letter] for letter in user_input]
print(result)
