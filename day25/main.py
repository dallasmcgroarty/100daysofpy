# data = []

# with open('day25/weather_data.csv') as file:
#   for line in file.readlines():
#     data.append(line.strip())

# print(data)

# using csv to read csv file
import csv

with open('day25/weather_data.csv') as file:
  data = csv.reader(file)
  temps = []
  for row in data:
    if row[1] != 'temp':
      temps.append(int(row[1]))

print(temps)

# using pandas
import pandas

data = pandas.read_csv('day25/weather_data.csv')
# print(data['temp'])
# print(data)

# convert panda dataframe to dict
data_dict = data.to_dict()
print(data_dict)

# convert pandas column to list'
temp_list = data['temp'].to_list()
print(len(temp_list))

# get average temp
# avg_temp = sum(temp_list) / len(temp_list)

mean_temp = data['temp'].mean()
print(mean_temp)

# get max value temp
max_temp = data['temp'].max()
print(max_temp)

# get data in columns
data['condition']
# pandas converts column headers to attributes
print(data.condition)

#get data in row
print(data[data.day == 'Monday'])

# get row with highest temp
print(data[data.temp == data.temp.max()])

# get monday temp in fahrenheit
mon_temp = data[data.day == 'Monday'].temp[0]
print((mon_temp * (9/5)) + 32)

# create dataframe from scratch
data_dict = {
  'students': ['Amy','Josh','Bill'],
  'scores': [76, 56, 65]
}
dict_to_data = pandas.DataFrame(data_dict)

# save to csv
dict_to_data.to_csv('day25/new_data.csv')
