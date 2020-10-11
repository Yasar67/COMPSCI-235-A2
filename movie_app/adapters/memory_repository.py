from movie_app.adapters.repository import AbstractRepository
from movie_app.adapters.domain.model import MovieFileCSVReader

class MemoryRepository(AbstractRepository):

    def __init__(self, reader: MovieFileCSVReader):
        self._movies = reader.dataset_of_movies
        self._directors = reader.dataset_of_directors
        self._actors = reader.dataset_of_actors
        self._genre = reader.dataset_of_genres

    def get_movies(self):
        return self._movies

