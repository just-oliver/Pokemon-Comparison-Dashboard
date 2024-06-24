
import numpy as np
import requests

def get_pokedict():
    pokedict = {}
    for poke_number in range(1,152):
        try:
            url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
            response = requests.get(url)
            pokemon = response.json()
            pokedict[pokemon['name'].title()] = poke_number
        except:
            pokedict['Error'] = np.poke_number
    return pokedict

def get_weights():
    weights = []
    for poke_number in range(1,152):
        try:
            url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
            response = requests.get(url)
            pokemon = response.json()
            weights.append(pokemon['weight']/10)
        except:
            weights.append(np.nan)
    return weights

def get_details(poke_number):
    try:
        url = f'https://pokeapi.co/api/v2/pokemon/{poke_number}/'
        response = requests.get(url)
        pokemon = response.json()
        type_dict = pokemon['types']
        if len(type_dict) > 1:
            types = []
            for t in type_dict:
                types.append(t['type']['name'])
            types = ' & '.join(types)
        else:
            types = type_dict[0]['type']['name']
        return pokemon['name'], pokemon['height'], pokemon['weight'], len(pokemon['moves']), len(pokemon['abilities']), types, pokemon['sprites']['other']['official-artwork']['front_default'], pokemon['cries']['latest']
    except:
        return 'Error', np.nan, np.nan, np.nan, np.nan, np.nan, np.nan, np.nan