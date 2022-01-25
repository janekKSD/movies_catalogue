import requests
from random import sample

API_TOKEN ="eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2ZDc1MTkwZTg2M2JhNDU2YmNmMWQ2Y2YwMTZhMzU1ZiIsInN1YiI6IjYxZTg0Nzg5YmM4NjU3MDA0MzE3MTNiYSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.lj9a6DFtw3zXyN2g6zRpcCwChtMtgsjoVojUSaEI_zw"

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_movies_list(list_type):
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    return response.json()

def get_movies(how_many, list_type):
    data = get_movies_list(list_type)
    return data["results"][:how_many]

def get_poster_url(poster_api_path, size="w342"):
    base_url = "https://image.tmdb.org/t/p/"
    return f"{base_url}{size}/{poster_api_path}"

def get_random_movies(how_many):
    data = get_popular_movies()
    return sample(data['results'], how_many)

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]


def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_genres():
    endpoint = "https://api.themoviedb.org/3/genre/movie/list"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()
