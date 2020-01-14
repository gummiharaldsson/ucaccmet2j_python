import json

with open('precipitation.json', encoding='utf8') as file:
     data = json.load(file)

# selecting only station seattle:
station_number = 'US1WAKG0038'
for datum in data:
    if datum['station'] == 'GHCND:US1WAKG0038':
        print(datum)