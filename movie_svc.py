import requests
from collections import namedtuple

MovieResult = namedtuple(
    'MovieResult',
    "imdb_code,title,duration,director,year,rating,imdb_score,keywords,genres")

def find_movies(search_text):
    url = f'http://movie_service.talkpython.fm/api/search/{search_text}'

    #TODO: Prevent empty searches
    if not search_text or not search_text.strip():
        #creating vs handling exceptions
        raise ValueError("Search text is required")

    resp = requests.get(url)
    resp.raise_for_status()

    movie_data = resp.json()
    movies_list = movie_data.get('hits')

    # Creates the list of MovieResult namedtuples with kwargs and a list comprehension.
    movies = [MovieResult(**md) for md in movies_list]

    # Performs a lambda function so that movies are sorted by year.
    movies.sort(key=lambda m: -m.year)

    return movies