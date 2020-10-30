from sqlalchemy import (
    Table, MetaData, Column, Integer, String
)
from sqlalchemy.orm import mapper

from movie_app.adapters.domain import model

metadata = MetaData()

movie = Table(
    'movie', metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('title', String(50), nullable=False),
    Column('genre', String(50), nullable=False),
    Column('description', String(1024), nullable=False),
    Column('director', String(50), nullable=False),
    Column('actors', String(200), nullable=False),
    Column('release_year', Integer, nullable=False),
    Column('runtime_minutes', Integer, nullable=False),
    Column('rating', Integer, nullable=False),
    Column('votes', Integer, nullable=False),
    Column('revenue', Integer, nullable=False),
)


def map_model_to_tables():
    mapper(model.Movie, movie, properties={
        '_id': movie.c.id,
        '_title': movie.c.title,
        '_genre': movie.c.genre,
        '_description': movie.c.description,
        '_director': movie.c.director,
        '_actors': movie.c.actors,
        '_release_year': movie.c.release_year,
        '_runtime_minutes': movie.c.runtime_minutes,
        '_rating': movie.c.rating,
        '_votes': movie.c.votes,
        '_revenue': movie.c.revenue,
    })
