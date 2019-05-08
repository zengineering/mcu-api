import falcon
import logging
import json
import msgpack
from .errors import DatabaseError
from .constants import MCUAPI_URL

def set_content_type(req, resp, resource):
    resp.content_type = falcon.MEDIA_MSGPACK
    resp.status = falcon.HTTP_OK

class Film():
    def __init__(self, db):
        self._db = db
        self.log = logging.getLogger(__name__)

    # @falcon.after(set_content_type)
    def on_get(self, req, resp, index=None):
        if index is not None:
            self.get_film(req, resp, index)
        else:
            raise falcon.HTTPNotFound()

    def get_film(self, req, resp, index):
        try:
            index = int(index)
            film = self._db.film(index)
            resp.data = msgpack.dumps(film, use_bin_type=True)
            resp.content_type = falcon.MEDIA_MSGPACK
            resp.status = falcon.HTTP_OK
            self.log.debug('GET film %d', index)
        except (DatabaseError, ValueError):
            raise falcon.HTTPNotFound()
