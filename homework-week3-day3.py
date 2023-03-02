#!/usr/bin/python
import requests

class Pokemon:
    def __init__(self, name, height, weight):
        self.name = name
        # self.type = type              couldn't get type to work
        self.height = height
        self.weight = weight

    def __repr__(self):
        return f"<Pokemon | {self.name} {self.height} {self.weight}"

    def __str__(self):
        return f"{self.name.title()} is a Pokemon that resembles a starfish.\
                \nIt has a height of {self.height} and a weight of {self.weight}."

class PokemonAPI:
    base_url = "https://pokeapi.co/api/v2/"

    def __init__(self):
        pass

    def __get(self, name):
        request_url = f"{self.base_url}pokemon/{name}"
        pokemon_response = requests.get(request_url)
        if pokemon_response.ok:
            return pokemon_response.json()

    def get_pokemon_info(self, name):
        pokemon_info = self.__get(name)
        if pokemon_info:
            pokemon_name = pokemon_info['name']
            pokemon_height = pokemon_info['height']
            pokemon_weight = pokemon_info['weight']
            pokemon = Pokemon(pokemon_name, pokemon_height, pokemon_weight)
            return pokemon
            
client = PokemonAPI()
print(client.get_pokemon_info('staryu'))
