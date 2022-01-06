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
    
response = requests.get(f'{base_url}episodes/')

#list of episode objects
episodes = []

for episode in response.json():
    episodes.append(Episode(episode['episode_id'],
                            episode['title'],
                            episode['season'],
                            episode['air_date'],
                            episode['characters'],
                            episode['episode'],
                            episode['series']))

response = requests.get(f'{base_url}quotes/')

#list of quote objects
quotes = []

for quote in response.json():
    quotes.append(Quote(quote['quote_id'],
                        quote['quote'],
                        quote['author'],
                        quote['series']))

response = requests.get(f'{base_url}deaths/')

#list of death objects
deaths = []

for death in response.json():
    deaths.append(Deaths(death['death_id'],
                    death['death'],
                    death['cause'],
                    death['responsible'],
                    death['last_words'],
                    death['season'],
                    death['episode'],
                    death['number_of_deaths']))


