import pandas
from logo import logo
print(logo)
data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}


name = input("Enter a word: ").upper()
list_alphabets = list(name)

ans_list = [data_dict[letter] for letter in list_alphabets]
print(ans_list)