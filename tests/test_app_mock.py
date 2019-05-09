import falcon
import pytest
from falcon import testing
from unittest.mock import call, MagicMock
from urllib.parse import urljoin

import mcuapi.app

@pytest.fixture
def mockery():
    return MagicMock()


@pytest.fixture
def client(mockery):
    api = mcuapi.app.create_app(mockery)
    return testing.TestClient(api)


def test_get_film_mock(mockery, client, film):
    film_id = film['id']
    mockery.film.return_value = film
    client.simulate_get('/films/{}'.format(film_id))
    mockery.film.assert_called_once_with(film_id)


def test_get_films_mock(mockery, client):
    mockery.films.return_value = []
    client.simulate_get('/films')
    mockery.films.assert_called_once()

