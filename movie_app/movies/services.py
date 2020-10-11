from movie_app.adapters.repository import AbstractRepository


def get_movies(repo: AbstractRepository):
    return repo.get_movies()
