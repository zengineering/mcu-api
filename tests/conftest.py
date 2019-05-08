import mountepy
import os
import sys
import pytest
from falcon import testing
from unittest.mock import mock_open, call, MagicMock
from mcuapi.database import Database
import mcuapi.app

@pytest.fixture
def mock_store():
    return MagicMock()

@pytest.fixture
def db():
    yield Database()

@pytest.fixture
def client(db):
    api = mcuapi.app.create_app(db)
    return testing.TestClient(api)

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


