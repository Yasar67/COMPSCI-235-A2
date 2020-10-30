import abc

from movie_app.adapters.domain.model import Movie

repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def get_movies(self):
        raise NotImplementedError
