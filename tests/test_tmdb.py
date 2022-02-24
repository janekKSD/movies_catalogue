import tmdb_client, requests
from unittest.mock import Mock

def test_get_single_movie_short():
    single_movie = tmdb_client.get_single_movie_short(movie_id=2)
    assert single_movie is not None 

def test_get_poster_url():
    poster_api_path = "poster_api_path"
    size = "size"
    poster_url = tmdb_client.get_poster_url(poster_api_path=poster_api_path, size=size)
    assert poster_url == "https://image.tmdb.org/t/p/size/poster_api_path"

def test_get_single_movie_cast_short():
    single_movie_casts = tmdb_client.get_single_movie_cast_short(movie_id=2)
    assert single_movie_casts is not None

def test_get_single_movie_cast(monkeypatch):
   mock_cast = {"cast": ["Janusz Janusz", "Beata i Asia"]}
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = mock_cast
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   movie_cast = tmdb_client.get_single_movie_cast(movie_id=2)
   assert movie_cast == mock_cast["cast"]

def test_get_movie_images(monkeypatch):
   movie_image = ["image"]
   requests_mock = Mock()
   response = requests_mock.return_value
   response.json.return_value = movie_image
   monkeypatch.setattr("tmdb_client.requests.get", requests_mock)
   get_movie_image = tmdb_client.get_movie_images(movie_id=2)
   assert get_movie_image == movie_image

