import json

with open('precipitation.json', encoding='utf8') as file:
     data = json.load(file)

# Part 2: calculating the sum of the precipitation over the whole year
station_number = 'US1WAKG0038'

total_precipitation = 0

for datum in data:
    if datum['station'] == 'GHCND:US1WAKG0038':
        precipitation_value = datum['value']
        print(precipitation_value)
        total_precipitation = total_precipitation + precipitation_value
print(total_precipitation)
# Answer is 11180
