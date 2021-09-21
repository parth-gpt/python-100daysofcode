# Read from file
# with open("my_file.txt") as file:
#     contents = file.read()
#     print(contents)

# Write to a file
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text.")
