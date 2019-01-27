import requests
from collections import namedtuple

#TODO: Offer user input for search
search = 'capital'
url = f'http://movie_service.talkpython.fm/api/search/{search}'

#TODO: Expand on namedtuple
MovieResult = namedtuple(
    'MovieResult',
    "imdb_code, title, duration, director, year, rating, imdb_score, keywords, genres")


# Use the requests library to pull the JSON data from the URL
resp = requests.get(url)

# Raises an error for status codes that are not 200.
# TODO: Go over status codes.
resp.raise_for_status()
print(resp.status_code)

# Could use resp.text(), but resp.json() is represented as a dict object in Python automagically.
movie_data = resp.json()

# Dictionary value for 'hits'
movies_list = movie_data.get('hits')
print(type(movies_list), movies_list)

# # Creating a new empty list for namedtuples of movies
# movies = []

# Creates named tuples with keyword arguments from our dictionary object. (non-Pythonic)
# for md in movies_list:
#     m = MovieResult(
#         imdb_code=md.get('imdb_code'),
#         title=md.get('title'),
#         duration=md.get('duration'),
#         director=md.get('director'),
#         year=md.get('year'),
#         rating=md.get('rating'),
#         imdb_score=md.get('imdb_score'),
#         keywords=md.get('keywords'),
#         genres=md.get('genres'),
#     )
#     movies.append(m)

# Using keyword arguments for a more Pythonic, extensible version.
# for md in movies_list:
#     m = MovieResult(**md)
#     movies.append(m)

# Using a list comprehension for the most Pythonic version.
movies = [MovieResult(**md) for md in movies_list]

# Displays movies
print(f'Found {len(movies)} for search {search}')
for m in movies:
    print(f'{m.title} -- {m.year}')

