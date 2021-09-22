import pandas

data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])

# dict_data = data.to_dict()
# print(dict_data)

# Average Temperature

# Normal Way
# temp_list = data["temp"].to_list()
# list_len = len(temp_list)
# sum = 0
# for i in temp_list:
#     sum += i
# sum = sum(temp_list)
# avg_temp = sum / list_len
# print(avg_temp)

# Pandas Way
# print(data["temp"].mean())

# Max Temperature
# print(data["temp"].max())

# Get Data in columns
# print(data["condition"])
# print(data.condition)

# Get Data in Row
# print(data[data.day == "Monday"])

# max_temp = data.temp.max()
# print(data[data.temp == max_temp])

# monday = data[data.day == "Monday"]
# monday_temp = int(monday.temp)
# farheniet = (monday_temp * 9/5) + 32
# print(farheniet)

# Create a dataframe from scratch

data_dict = {
    "students" : ["Amy", "James", "Angela"],
    "scores" : [76, 56, 65]
}

data = pandas.DataFrame(data_dict)
data.to_csv("new_data.csv")
print(data)
