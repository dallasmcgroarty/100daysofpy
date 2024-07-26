import pandas

data = pandas.read_csv('day25/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

gray_squirrel_count = len(data[data['Primary Fur Color'] == 'Gray'])
red_squirrel_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
black_squirrel_count = len(data[data['Primary Fur Color'] == 'Black'])

squirrels = {
  'Fur color': ['Gray','Red','Black'],
  'Count': [gray_squirrel_count, red_squirrel_count, black_squirrel_count]
}

df = pandas.DataFrame(squirrels)

# save to csv
df.to_csv('day25/squirrel_color_count.csv')