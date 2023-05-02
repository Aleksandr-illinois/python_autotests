import requests
import pytest
TOKEN = '2c4a58d6d5b9b053fb9dd0eb7c8e9e49'
HOST = 'https://pokemonbattle.me:9104/'

def test_status_code():
    response = requests.get(f'{HOST}trainers')
    assert response.status_code == 200




def test_name_id():
    response = requests.get(f'{HOST}trainers',params={'trainer_id': 4250})
    assert response.json()['trainer_name'] == 'dubina'