import json

with open('precipitation.json', encoding='utf8') as file:
     data = json.load(file)

# Part 2: calculating the sum of the precipitation over the whole year
station_number = 'US1WAKG0038'

# Total precipitation for whole year and per month
total_precipitation = 0
precipitation_per_month = [0]*12

for datum in data:
    if datum['station'] == 'GHCND:US1WAKG0038':
        
        precipitation_value = datum['value']
        total_precipitation = total_precipitation + precipitation_value

        date = datum['date']
        month = int(date[5:7])
        rainfall = datum['value']
        precipitation_per_month[month-1] += rainfall

# Finding percentage precipitation
percentage_precipitation = []
for precipitation in precipitation_per_month:
    percentage_precipitation.append(precipitation/total_precipitation)
print(percentage_precipitation)

# print(precipitation_per_month)
# print(total_precipitation)
# [1693, 730, 870, 752, 924, 601, 54, 104, 996, 908, 1192, 2356]
# Answer is 11180
