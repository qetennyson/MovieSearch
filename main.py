import requests
from collections import namedtuple

search = 'capital'
url = f'http://movie_service.talkpython.fm/api/search/{search}'

MovieResult = namedtuple(
    'MovieResult',
    "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")


resp = requests.get(url)
resp.raise_for_status()

movie_data = resp.json()
movies_list = movie_data.get('hits')

print(resp.status_code)
print(type(movies_list), movies_list)

movies = []
for md in movies_list:
    m = MovieResult(
        imdb_code=md.get('imdb_code'),
        title=md.get('title'),
        duration=md.get('duration'),
        director=md.get('director'),
        year=md.get('year'),
        rating=md.get('rating'),
        imdb_score=md.get('imdb_score'),
        keywords=md.get('keywords'),
        genres=md.get('genres'),
    )
    movies.append(m)

print(f'Found {len(movies)} for search {search}')
for m in movies:
    print(f'{m.title} -- {m.year}')

