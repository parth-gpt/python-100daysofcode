data1 = []
data2 = []
with open("file1.txt") as file1:
    data = file1.readlines()
    for i in data:
        new_data = int(i.strip())
        data1.append(new_data)

with open("file2.txt") as file2:
    data = file2.readlines()
    for i in data:
        new_data = int(i.strip())
        data2.append(new_data)

result = [n for n in data1 if n in data2]

print(result)