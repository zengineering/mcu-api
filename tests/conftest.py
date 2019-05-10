import mountepy
import os
import sys
import pytest
from falcon import testing
from unittest.mock import mock_open, call, MagicMock
from mcuapi.database import Database
import mcuapi.app

@pytest.fixture
def mockery():
    return MagicMock()

@pytest.fixture
def db(scope='session'):
    yield Database()

@pytest.fixture(scope='session')
def the_gunicorn():
    gunicorn_path = os.path.join(os.path.dirname(sys.executable), 'gunicorn')

    service_command = [
        gunicorn_path,
        'mcuapi.app:get_app()',
        '--bind', ':{port}',
        '--enable-stdio-inheritance',
        '--pythonpath', ','.join(sys.path)
    ]

    with mountepy.HttpService(service_command, port=8000) as service:
        yield service


@pytest.fixture
def character():
    return {
        "name": "Korg",
        "alter-ego": "None",
        "actors": [
            "Taika Waititi"
        ],
        "id": 26,
        "films" : [
            17, 22
        ]
    }

@pytest.fixture
def film():
    return {
        "title": "Captain America: The Winter Soldier",
        "release": "04 April 2014",
        "director": "Anthony and Joe Russo",
        "id": 9,
        "runtime": 136,
        "box-office-usa": 259.8,
        "box-office-world": 714.3,
        "rotten-tomatoes-critic": 90,
        "rotten-tomatoes-audience": 92
    }
