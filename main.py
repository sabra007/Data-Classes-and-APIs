from dataclasses import dataclass
import requests

@dataclass
class Character:
    id: int
    name: str
    birthday: str
    occupation: list
    img: str
    status: str
    nickname: str
    appearacnce: list
    portrayed: str
    category: list

@dataclass
class Episode:
    id: int
    title: str
    season: int
    episode: int
    air_date: str
    characters: list
    series: str
    
@dataclass
class Quote:
    id: int
    quote: str
    author: str
    series: str

@dataclass
class Deaths:
    id: int
    death: str
    cause: str
    responsible: str
    last_words: str
    season: int
    episode: int
    number_of_deaths: int

# pulling character data from api

base_url = 'https://www.breakingbadapi.com/api/'
response = requests.get(f'{base_url}characters/')

# list of character objects
characters = []

for character in response.json():
    characters.append(Character(character['char_id'], 
                                character['name'], 
                                character['birthday'], 
                                character['occupation'], 
                                character['img'], 
                                character['status'], 
                                character['nickname'], 
                                character['appearance'], 
                                character['portrayed'], 
                                character['category']))


