import falcon
import msgpack
import pytest
import re
from falcon import testing

import mcuapi.app
from mcuapi.constants import MCUAPI_URL
from mcuapi.schema import FilmSchema, CharacterSchema
from mcuapi.content import Content


@pytest.fixture
def client(db):
    api = mcuapi.app.create_app(db)
    return testing.TestClient(api)


@pytest.fixture
def film_re():
    return re.compile('/'.join((MCUAPI_URL, 'films', '\\d+')))


@pytest.fixture
def character_re():
    return re.compile('/'.join((MCUAPI_URL, 'characters', '\\d+')))


@pytest.fixture
def api_path():
    return "api"


def test_get_film(client, film):
    '''
    Get a specific film record
    '''
    response = client.simulate_get('/api/films/9')
    assert response.status == falcon.HTTP_OK
    result = msgpack.loads(response.content, raw=False)
    assert result == film


def test_get_film_fail(client):
    '''
    Get a nonexistent film record
    '''
    response = client.simulate_get('/api/films/999')
    assert response.status == falcon.HTTP_NOT_FOUND


def test_get_films(client, db, film_re):
    '''
    Get all films (list of urls with film id)
    '''
    response = client.simulate_get('/api/films')
    assert response.status == falcon.HTTP_OK
    result = msgpack.loads(response.content, raw=False)
    assert len(result) == db.film_count
    assert all([film_re.match(film) for film in result])


def test_get_film_schema(client, db):
    response = client.simulate_get('/api/films/schema')
    assert response.status == falcon.HTTP_OK
    result = msgpack.loads(response.content, raw=False)
    assert result == db.film_schema


def test_get_character(client, character):
    '''
    Get a specific character record
    '''
    response = client.simulate_get('/api/characters/26')
    assert response.status == falcon.HTTP_OK
    result = msgpack.loads(response.content, raw=False)
    assert result == character


def test_get_character_fail(client):
    '''
    Get a nonexistent character record
    '''
    response = client.simulate_get('/api/characters/999')
    assert response.status == falcon.HTTP_NOT_FOUND


def test_get_characters(client, db, character_re):
    '''
    Get all characters (list of urls with character id)
    '''
    response = client.simulate_get('/api/characters')
    assert response.status == falcon.HTTP_OK
    result = msgpack.loads(response.content, raw=False)
    assert len(result) == db.character_count
    assert all([character_re.match(character) for character in result])


def test_get_character_schema(client, db):
    response = client.simulate_get('/api/characters/schema')
    assert response.status == falcon.HTTP_OK
    result = msgpack.loads(response.content, raw=False)
    assert result == db.character_schema


def test_get_contents(client):
    response = client.simulate_get('/api')
    assert response.status == falcon.HTTP_OK
    result = msgpack.loads(response.content, raw=False)
    assert result == Content._CONTENT

