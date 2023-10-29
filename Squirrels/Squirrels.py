#Created by Shlomi Kiko
#Goal: Reads from a csv file, focuses on a specific column, aggregated into counts for colors and writes into a new csv file.
#LinkedIn: https://www.linkedin.com/in/shlomikiko/

import pandas as pd

#Read file
df_centralParkSquirrels = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
#Focus on the specific column
columnToFocus = 'Primary Fur Color'
df_squirrelsPrimaryColor = df_centralParkSquirrels[columnToFocus]
#Group by color, to get an idea of how much we have for each
df_groupedSquirrelsPrimaryColor = df_squirrelsPrimaryColor.groupby(df_squirrelsPrimaryColor).count()
#Convert from Series to Dictionary
dictGroupedSquirrels = df_groupedSquirrelsPrimaryColor.to_dict()
#Add some key for Header names later and group the keys and values accordingly
dictGroupedSquirrels = {'Fur Color': dictGroupedSquirrels.keys(), 'Count': dictGroupedSquirrels.values()}
#Convert from a dictionary into a dataframe
df_groupedSquirrels = pd.DataFrame(dictGroupedSquirrels, index=['a', 'b', 'c'])
#Finally write the data into a new CSV file
groupedSquirrelsCsv = df_groupedSquirrels.to_csv('GroupedSquirrels.csv')

print(f'Aggregations for column: "{columnToFocus}" written to a new Csv file.')
