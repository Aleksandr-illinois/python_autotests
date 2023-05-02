import requests
TOKEN = '2c4a58d6d5b9b053fb9dd0eb7c8e9e49'
HOST = 'https://pokemonbattle.me:9104/'
response_reg_trainer = requests.post(f'{HOST}trainers/reg', json={
    "trainer_token": TOKEN,
    "email": "german@dolnikov.ru",
    "password": "Iloveqa1"
})
print(response_reg_trainer.text)

response_activeted_trainer = requests.post(f'{HOST}trainers/confirm_email', json={
    "trainer_token": TOKEN
})
print(response_activeted_trainer.text)

response_add_pokemon = requests.post(f'{HOST}pokemons', headers={"trainer_token": TOKEN}, json={
    "name": "Пармалат",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
})
print(response_add_pokemon.text)




response_name_pokemon = requests.put(f'{HOST}pokemons', headers={"trainer_token": TOKEN}, json={
    "pokemon_id": "9791",
    "name": "Гаврюша",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(response_name_pokemon.text)


response_add_pokeball = requests.post(f'{HOST}trainers/add_pokeball', headers={"trainer_token": TOKEN}, json={
    "pokemon_id": "9670"
})
print(response_add_pokeball.text)


{'id': '4250', 'trainer_name': 'dubina', 'trainer_token': '2c4a58d6d5b9b053fb9dd0eb7c8e9e49'}