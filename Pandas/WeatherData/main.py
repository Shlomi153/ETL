import csv
import pandas

# with open('./weather_data.csv', 'r') as weather_data:
#     data_csv = csv.reader(weather_data)
#     temp_list = []

#     for i in data_csv:
#         if i[1] != 'temp':
#             temp_list.append(i[1])

# print(temp_list)

weather_data = pandas.read_csv('./weather_data.csv')

temp_list = weather_data.temp.to_list()
temp_list = [int(n) for n in temp_list]

# print(temp_list)

sum = sum(temp_list)
count = len(temp_list)
avg_temp = round(sum / count, 2)

# print(avg_temp)

max = max(temp_list)

# print(max)

# print(round(weather_data["temp"].mean(), 2))
# print(round(weather_data["temp"].max(), 2))

# print(weather_data[weather_data.day == "Tuesday"])
# print(weather_data[weather_data.temp == weather_data.temp.max()])

sunday = weather_data.loc[weather_data.day == "Sunday"]
sunday_temp = sunday.temp.values[0]

# cel_to_fahr_sunday = (sunday_temp * 1.8) + 32

print(sunday_temp)
# print(cel_to_fahr_sunday)

# avg_temp = round(weather_data.temp.mean(), 2)

# print(avg_temp)

data_dict = {
    "Students": ["Dany", "Lizzie", "Dana", "Robert"],
    "Grades": [82, 32, 54, 66]
}

print(data_dict)

df_data = pandas.DataFrame(data_dict)

print(df_data)

df_data.to_csv('StudentGrades.csv')