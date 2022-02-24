from flask import Flask, render_template, make_response, jsonify, request
import tmdb_client

app = Flask(__name__)
type_list = {"popular": "Popularne", "now_playing": "Na czasie", "top_rated": "Najelpiej oceniane", "upcoming": "Wkrótce"}

@app.route('/')
def homepage():
    selected_list = request.args.get('list_type', 'popular')
    if selected_list not in type_list:
        selected_list = 'popular'
    how_many = tmdb_client.create_int(request.args.get('how_many', 8))
    movies = tmdb_client.get_movies(how_many, list_type=selected_list)
    genres = tmdb_client.get_genres()['genres']
    genre_id = tmdb_client.create_int(request.args.get('genre_id', 0))
    

    return render_template("homepage.html", movies=movies, current_list=selected_list, genres=genres, genre_id=genre_id, type_list=type_list, how_many=how_many)

@app.context_processor
def utility_processor():
    def tmdb_image_url(path, size):
        return tmdb_client.get_poster_url(path, size)
    return {"tmdb_image_url": tmdb_image_url}

@app.route("/movie/<movie_id>")
def movie_details(movie_id):
    details = tmdb_client.get_single_movie(movie_id)
    cast = tmdb_client.get_single_movie_cast(movie_id)
    print(cast)
    return render_template("movie_details.html", movie=details, cast=cast)

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error(r)': 'Not found(d)', 'status_code(e)': 404}), 404)

@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error(r)': 'Bad request(t)', 'status_code(e)': 400}), 400)

if __name__ == '__main__':
    app.run(debug=True)

