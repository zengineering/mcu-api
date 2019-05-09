import falcon
import pytest
from falcon import testing
from unittest.mock import call, MagicMock
from urllib.parse import urljoin

import mcuapi.app

@pytest.fixture
def mock_db():
    return MagicMock()


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
    client.simulate_get('/films/{}'.format(film_id))
    mock_db.film.assert_called_once_with(film_id)


def test_get_films_mock(mock_db, client):
    '''
    proper db method is called for /films
    '''
    mock_db.films.return_value = []
    client.simulate_get('/films')
    mock_db.films.assert_called_once()


def test_get_char_mock(mock_db, client, character):
    '''
    proper db method is called for /characters/{}
    '''
    character_id = character['id']
    mock_db.character.return_value = character
    client.simulate_get('/characters/{}'.format(character_id))
    mock_db.character.assert_called_once_with(character_id)


def test_get_chars_mock(mock_db, client):
    '''
    proper db method is called for /characters
    '''
    mock_db.characters.return_value = []
    client.simulate_get('/characters')
    mock_db.characters.assert_called_once()


def test_get_bad_routes(client):
    response = client.simulate_get('/invalid/route/')
    assert response.status == falcon.HTTP_NOT_FOUND
    response = client.simulate_get('/character/1')
    assert response.status == falcon.HTTP_NOT_FOUND
    response = client.simulate_get('/film/1')
    assert response.status == falcon.HTTP_NOT_FOUND

