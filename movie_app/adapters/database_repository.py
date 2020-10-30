import csv
import os
from abc import ABC

from typing import List

from sqlalchemy import desc, asc
from sqlalchemy.engine import Engine
from sqlalchemy.orm.exc import NoResultFound, MultipleResultsFound

from sqlalchemy.orm import scoped_session
from flask import _app_ctx_stack

from movie_app.adapters.domain.model import Movie
from movie_app.adapters.repository import AbstractRepository


class SessionContextManager:
    def __init__(self, session_factory):
        self.__session_factory = session_factory
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.rollback()

    @property
    def session(self):
        return self.__session

    def commit(self):
        self.__session.commit()

    def rollback(self):
        self.__session.rollback()

    def reset_s_cession(self):
        # this method can be used e.g. to allow Flask to start a new session for each http request,
        # via the 'before_request' callback
        self.close_current_session()
        self.__session = scoped_session(self.__session_factory, scopefunc=_app_ctx_stack.__ident_func__)

    def close_current_session(self):
        if not self.__session is None:
            self.__session.close()


class SqlAlchemyRepository(AbstractRepository, ABC):

    def __init__(self, session_factory):
        self._session_cm = SessionContextManager(session_factory)

    def close_session(self):
        self._session_cm.close_current_session()

    def reset_session(self):
        self._session_cm.reset_session()

    def add_movie(self, movie: Movie):
        with self._session_cm as scm:
            scm.session.add(movie)
            scm.commit()

    def get_movie(self, title) -> Movie:
        movie = None
        try:
            user = self._session_cm.session.query(Movie).filter_by(_title=title).one()
        except NoResultFound:
            # Ignore any exception and return None.
            pass

        return movie

    def get_movies(self) -> List[Movie]:
        movies = self._session_cm.session.query(Movie).all()

        return movies

    def get_number_of_movies(self):
        number_of_articles = self._session_cm.session.query(Movie).count()
        return number_of_articles

    def get_first_movie(self):
        article = self._session_cm.session.query(Movie).first()
        return article

    def get_last_movie(self):
        article = self._session_cm.session.query(Movie).order_by(desc(Movie._id)).first()
        return article


def movie_record_generator(filename: str):
    with open(filename, mode='r', encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        headers = next(reader)

        for row in reader:
            movie_data = row
            movie_key = movie_data[0]

            # Strip any leading/trailing white space from data read.
            movie_data = [item.strip() for item in movie_data]
            del movie_data[-1]

            yield movie_data


def populate(engine: Engine, data_path: str):
    conn = engine.raw_connection()
    cursor = conn.cursor()

    insert_movie = """
        INSERT INTO movie (
         id, title, genre, description, director, actors, 
         release_year, runtime_minutes, rating, votes, revenue)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)"""

    cursor.executemany(insert_movie, movie_record_generator(os.path.join(data_path, 'Data1000Movies.csv')))

    conn.commit()
    conn.close()
