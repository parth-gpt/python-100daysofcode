import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [len(data[data["Primary Fur Color"] == "Gray"]), len(data[data["Primary Fur Color"] == "Cinnamon"]),
              len(data[data["Primary Fur Color"] == "Black"])]
}
data = pandas.DataFrame(data_dict)
data.to_csv("squirel_count.csv")
print(data)
