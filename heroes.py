import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
heroes = ['Hulk', 'Captain America', 'Thanos']
response = requests.get(url).json()
heroes_dict = dict()

for i in response:
    for c, d in i.items():
        if d in heroes:
            for key, values in i.items():
                if key == 'powerstats':
                    heroes_dict[d] = values['intelligence']
print(max(heroes_dict))