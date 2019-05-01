import mountepy, os, sys, pytest

@pytest.fixture
def mock_store():
    return MagicMock()

@pytest.fixture
def client(mock_store):
    api = falconplay.app.create_app(mock_store)
    return testing.TestClient(api)

@pytest.fixture(scope='session')
def the_gunicorn():
    gunicorn_path = os.path.join(os.path.dirname(sys.executable), 'gunicorn')

    service_command = [
        gunicorn_path,
        'mcu-api.app:get_app()',
        '--bind', ':{port}',
        '--enable-stdio-inheritance',
        '--pythonpath', ','.join(sys.path)
    ]

    with mountepy.HttpService(service_command, port=8000) as service:
        yield service


