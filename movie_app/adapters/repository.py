import abc

from movie_app.adapters.domain.model import Movie

repo_instance = None

class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_movies(self):
        raise NotImplementedError
