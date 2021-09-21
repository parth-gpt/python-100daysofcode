PLACEHOLDER = "[name]"
with open("./Input/Names/invited_names.txt", mode="r") as names_file:
    names = names_file.readlines()

with open("./Input/Letters/starting_letter.txt", mode="r") as letters_file:
    letter = letters_file.read();
    for name in names:
            new_name = name.strip()
            new_letter = letter.replace(PLACEHOLDER, new_name)
            with open(f"./Output/ReadyToSend/letter_for_{new_name}.txt", mode="w") as completed_letter:
                completed_letter.write(new_letter)