from sqlalchemy import select, inspect

from movie_app.adapters.orm import metadata


def test_database_populate_inspect_table_names(database_engine):
    # Get table information
    inspector = inspect(database_engine)
    assert inspector.get_table_names() == ['movies']


def test_database_populate_select_all_articles(database_engine):
    # Get table information
    inspector = inspect(database_engine)
    name_of_movies_table = inspector.get_table_names()[1]

    with database_engine.connect() as connection:
        # query for records in table movies
        select_statement = select([metadata.tables[name_of_movies_table]])
        result = connection.execute(select_statement)

        all_movies = []
        for row in result:
            all_movies.append((row['id'], row['title']))

        nr_movies = len(all_movies)

        assert all_movies[0] == (1, 'Guardians of the Galaxy')
        assert all_movies[nr_movies // 2] == (500, 'Up')
        assert all_movies[nr_movies - 1] == (999, 'Nine Lives')
