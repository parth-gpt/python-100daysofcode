# numbers = [1, 2, 3]
# ne_numbers = [n+1 for n in numbers]
# name = "Angela"
# name_list = [letter for letter in name]
# double_list = [n*2 for n in range(1, 5)]
# names = ["Alex", "Angela","Dave", "Parth", "Fredi"]
# new_names = [name for name in names if len(name) == 5]
# print(names)
# new_names_list = [name.upper() for name in names if len(name) >= 5]
# print(new_names_list)

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

squared_numbers = [n**2 for n in numbers]

print(squared_numbers)