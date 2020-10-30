import pytest


from movie_app.adapters.domain.model import Movie


def insert_movie(empty_session):
    empty_session.execute(
        'INSERT INTO articles (id, title, genre, description, director, actors, release_year, runtime_minutes, '
        'rating, votes, revenue) VALUES '
        '1001', '"The Last Airbender"', 'Adventure', '"I believe Aang can save the world"', '"Taika Watiti"',
        'John Snow', '2011', '149', '0', '1000', '20'
    )
    row = empty_session.execute('SELECT id from movies').fetchone()
    return row[0]


def make_movie():
    movie = Movie("Cyberpunk", 2077)
    return movie


def test_loading_of_movie(empty_session):
    movie_key = insert_movie(empty_session)
    expected_movie = make_movie()
    fetched_movie = empty_session.query(Movie).one()

    assert expected_movie == fetched_movie
    assert movie_key == fetched_movie.id


def test_saving_of_movie(empty_session):
    movie = make_movie()
    empty_session.add(movie)
    empty_session.commit()

    rows = list(empty_session.execute('title, release_year, FROM movies'))
    assert rows == [(
       '"Cyberpunk', '2077'
    )]
