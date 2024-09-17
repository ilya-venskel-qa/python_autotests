import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '01281ef7a09182cdae1d91cbcb1c4b79'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_create_pokemon = {
    "name": "generate",
    "photo_id": -1
}
body_put_name = {
    "pokemon_id": "71662",
    "name": "Patrik",
    "photo_id": 2
}
body_catch_pokemon = {
    "pokemon_id": "71662"
}

response = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create_pokemon )
print(response.text)

response_rename = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_put_name)
print(response_rename.text)

response_catch = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_catch_pokemon)
print(response_catch.text)

pokemon_id = response.json()[id]