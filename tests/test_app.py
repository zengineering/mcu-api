import falcon
import msgpack
import pytest
import io
from falcon import testing
from unittest.mock import mock_open, call, MagicMock

import mcuapi.app
import mcuapi.films

@pytest.fixture
def mock_store():
    return MagicMock()

@pytest.fixture
def client(mock_store):
    api = mcuapi.app.create_app(mock_store)
    return testing.TestClient(api)

def test_get_film(client):
    doc = {
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

    response = client.simulate_get('/films/9')
    assert response.status == falcon.HTTP_OK
    result_doc = msgpack.unpackb(response.content, encoding='utf-8')
    assert result_doc == doc

# def test_post_image(client, mock_store):
#     filename = 'fake-image-name.xyz'

#     mock_store.save.return_value = filename
#     image_content_type = 'image/xyz'

#     response = client.simulate_post (
#         '/images',
#         body=b'fake-image-bytes',
#         headers={'content-type': image_content_type}
#     )

#     assert response.status == falcon.HTTP_CREATED
#     assert response.headers['location'] == '/images/{}'.format(filename)
#     saver_call = mock_store.save.call_args

#     assert isinstance(saver_call[0][0], falcon.request_helpers.BoundedStream)
#     assert saver_call[0][1] == image_content_type


# def test_saving_image(monkeypatch):
#     mock_file_open = mock_open()

#     fake_uuid = '123e4567-e89b-12d3-a456-426655440000'

#     def mock_uuidgen():
#         return fake_uuid

#     fake_image_bytes = b'fake-image-bytes'
#     fake_request_stream = io.BytesIO(fake_image_bytes)
#     storage_path = 'fake-storage-path'
#     store = falconplay.images.ImageStore(
#         storage_path,
#         uuidgen=mock_uuidgen,
#         fopen=mock_file_open
#     )

#     assert store.save(fake_request_stream, 'image/png') == fake_uuid + '.png'
#     assert call().write(fake_image_bytes) in mock_file_open.mock_calls

