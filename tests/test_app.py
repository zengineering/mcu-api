import pytest
import falcon
import msgpack
import json
import re
from falcon import testing

import mcuapi.app
from mcuapi.constants import MCUAPI_URL
from mcuapi.schema import FilmSchema, CharacterSchema
from mcuapi.content import Content
from mcuapi.utils import MEDIA_HANDLERS


@pytest.fixture
def client(db):
    api = mcuapi.app.create_app(db, MEDIA_HANDLERS)
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


@pytest.mark.parametrize('fmt,unpacker', (
    ('msgpack', lambda data: msgpack.loads(data, raw=False)),
    ('json', json.loads),
    # ('', json.loads)
))
def test_get_film(client, film, fmt, unpacker):
    '''
    Get a specific film record
    '''
    params = {'format': fmt} if fmt else None
    response = client.simulate_get('/api/films/9', params=params)
    assert response.status == falcon.HTTP_OK
    result = unpacker(response.content)
    assert result == film


def test_get_film_fail(client):
    '''
    Get a nonexistent film record
    '''
    response = client.simulate_get('/api/films/999')
    assert response.status == falcon.HTTP_NOT_FOUND


@pytest.mark.parametrize('fmt,unpacker', (
    ('msgpack', lambda data: msgpack.loads(data, raw=False)),
    ('json', json.loads),
    # ('', json.loads)
))
def test_get_films(client, db, film_re, fmt, unpacker):
    '''
    Get all films (list of urls with film id)
    '''
    params = {'format': fmt} if fmt else None
    response = client.simulate_get('/api/films', params=params)
    assert response.status == falcon.HTTP_OK
    result = unpacker(response.content)
    assert len(result) == db.film_count
    assert all([film_re.match(film) for film in result])


@pytest.mark.parametrize('fmt,unpacker', (
    ('msgpack', lambda data: msgpack.loads(data, raw=False)),
    ('json', json.loads),
    # ('', json.loads)
))
def test_get_film_schema(client, db, fmt, unpacker):
    params = {'format': fmt} if fmt else None
    response = client.simulate_get('/api/films/schema', params=params)
    assert response.status == falcon.HTTP_OK
    result = unpacker(response.content)
    assert result == db.film_schema


@pytest.mark.parametrize('fmt,unpacker', (
    ('msgpack', lambda data: msgpack.loads(data, raw=False)),
    ('json', json.loads),
    # ('', json.loads)
))
def test_get_character(client, character, fmt, unpacker):
    '''
    Get a specific character record
    '''
    params = {'format': fmt} if fmt else None
    response = client.simulate_get('/api/characters/26', params=params)
    assert response.status == falcon.HTTP_OK
    result = unpacker(response.content)
    assert result == character


def test_get_character_fail(client):
    '''
    Get a nonexistent character record
    '''
    response = client.simulate_get('/api/characters/999')
    assert response.status == falcon.HTTP_NOT_FOUND


@pytest.mark.parametrize('fmt,unpacker', (
    ('msgpack', lambda data: msgpack.loads(data, raw=False)),
    ('json', json.loads),
    # ('', json.loads)
))
def test_get_characters(client, db, character_re, fmt, unpacker):
    '''
    Get all characters (list of urls with character id)
    '''
    params = {'format': fmt} if fmt else None
    response = client.simulate_get('/api/characters', params=params)
    assert response.status == falcon.HTTP_OK
    result = unpacker(response.content)
    assert len(result) == db.character_count
    assert all([character_re.match(character) for character in result])


@pytest.mark.parametrize('fmt,unpacker', (
    ('msgpack', lambda data: msgpack.loads(data, raw=False)),
    ('json', json.loads),
    # ('', json.loads)
))
def test_get_character_schema(client, db, fmt, unpacker):
    params = {'format': fmt} if fmt else None
    response = client.simulate_get('/api/characters/schema', params=params)
    assert response.status == falcon.HTTP_OK
    result = unpacker(response.content)
    assert result == db.character_schema


@pytest.mark.parametrize('fmt,unpacker', (
    ('msgpack', lambda data: msgpack.loads(data, raw=False)),
    ('json', json.loads),
    # ('', json.loads)
))
def test_get_contents(client, fmt, unpacker):
    params = {'format': fmt} if fmt else None
    response = client.simulate_get('/api', params=params)
    assert response.status == falcon.HTTP_OK
    result = unpacker(response.content)
    assert result == Content._CONTENT


def test_get_bad_routes(client):
    response = client.simulate_get('/api/invalid/route/')
    assert response.status == falcon.HTTP_NOT_FOUND
    response = client.simulate_get('/api/character/1')
    assert response.status == falcon.HTTP_NOT_FOUND
    response = client.simulate_get('/api/film/1')
    assert response.status == falcon.HTTP_NOT_FOUND

