from flask import Flask
from flask import Blueprint
import os

import movie_app.adapters.repository as repo
from movie_app.adapters.memory_repository import MemoryRepository
from movie_app.adapters.domain.model import MovieFileCSVReader

def create_app(test_config=None):

    app = Flask(__name__)

    app.config.from_object('config.Config')
    data_path = os.path.join('movie_app', 'adapters', 'Data', 'Data1000Movies.csv')

    if test_config is not None:

        app.config.from_mapping(test_config)
        data_path = app.config['TEST_DATA_PATH']

    reader = MovieFileCSVReader(data_path)
    reader.read_csv_file()

    repo.repo_instance = MemoryRepository(reader)

    with app.app_context():
        from .movies import movies
        app.register_blueprint(movies.movies_blueprint)

        from .home import home
        app.register_blueprint(home.home_blueprint)

        from .login import login
        app.register_blueprint(login.login_blueprint)


    return app