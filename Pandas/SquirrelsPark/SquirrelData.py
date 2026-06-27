#Created by Shlomi Kiko
#Goal: Reads from the Squirrel csv file, seperates it into series and then groups them together by Primary Fur Color
#LinkedIn: https://www.linkedin.com/in/shlomikiko/

import pandas as pd

squirrel_data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250815.csv')

gray_squirrels = squirrel_data[squirrel_data['Primary Fur Color'] == 'Gray']
cinnamon_squirrels = squirrel_data[squirrel_data['Primary Fur Color'] == 'Cinnamon']
black_squirrels = squirrel_data[squirrel_data['Primary Fur Color'] == 'Black']

total_gray_squirrels = len(gray_squirrels)
total_cinnamon_squirrels = len(cinnamon_squirrels)
total_black_squirrels = len(black_squirrels)

dict_squirrels = {
    'Primary Fur Color':['Gray', 'Cinnamon', 'Black'],
    'Total':[total_gray_squirrels, total_cinnamon_squirrels, total_black_squirrels]
}

df_squirrels_colors = pd.DataFrame(dict_squirrels)

print(df_squirrels_colors)