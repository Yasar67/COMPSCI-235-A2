from flask import Blueprint, render_template, request

from movie_app.movies import services

import movie_app.adapters.repository as repo

movies_blueprint = Blueprint(
    'movies_bp', __name__)


@movies_blueprint.route('/movies', methods=['GET'])
def movies():
    all_movies = services.get_movies(repo.repo_instance)

    return render_template('movies.html', movies=all_movies)
