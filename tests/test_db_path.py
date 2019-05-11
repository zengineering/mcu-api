import falcon
import pytest
from falcon import testing
from unittest.mock import call, MagicMock, PropertyMock
from urllib.parse import urljoin

import mcuapi.app

@pytest.fixture
def mock_db():
    return MagicMock()


@pytest.fixture
def mock_db_prop():
    return PropertyMock()


@pytest.fixture
def client(mock_db):
    '''
    test client with mock database
    '''
    api = mcuapi.app.create_app(mock_db)
    return testing.TestClient(api)


def test_get_film_mock(mock_db, client, film):
    '''
    proper db method is called for /film/{}
    '''
    film_id = film['id']
    mock_db.film.return_value = film
    client.simulate_get('/api/films/{}'.format(film_id))
    mock_db.film.assert_called_once_with(film_id)


def test_get_films_mock(mock_db, mock_db_prop, client):
    '''
    proper db method is called for /films
    '''
    mock_db_prop.return_value = {}
    type(mock_db).films = mock_db_prop
    client.simulate_get('/api/films')
    mock_db_prop.assert_called_once()


def test_get_film_schema_mock(mock_db, mock_db_prop, client):
    mock_db_prop.return_value = {}
    type(mock_db).film_schema = mock_db_prop
    client.simulate_get('/api/films/schema')
    mock_db_prop.assert_called_once()


def test_get_char_mock(mock_db, client, character):
    '''
    proper db method is called for /characters/{}
    '''
    character_id = character['id']
    mock_db.character.return_value = character
    client.simulate_get('/api/characters/{}'.format(character_id))
    mock_db.character.assert_called_once_with(character_id)


def test_get_chars_mock(mock_db, mock_db_prop, client):
    '''
    proper db method is called for /characters
    '''
    mock_db_prop.return_value = {}
    type(mock_db).characters = mock_db_prop
    client.simulate_get('/api/characters')
    mock_db_prop.assert_called_once()


def test_get_character_schema_mock(mock_db, mock_db_prop, client):
    mock_db_prop.return_value = {}
    type(mock_db).character_schema = mock_db_prop
    client.simulate_get('/api/characters/schema')
    mock_db_prop.assert_called_once()


