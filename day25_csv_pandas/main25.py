# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)

# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     print(data)
#     temperatures = []
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(float(row[1]))
#     print(temperatures)

# import pandas as pd
#
# data = pd.read_csv("weather_data.csv")
# print(data)

import pandas as pd


def read_the_file(file_name):
    return pd.read_csv(file_name)


data = read_the_file("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
# print(type(data))

print(data.info())

table = pd.pivot_table(data, values='X', index = 'Primary Fur Color')
print(table)
