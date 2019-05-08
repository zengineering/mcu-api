import falcon
import logging
import json
import msgpack
from .errors import DatabaseError

def set_content_type(req, resp, resource):
    resp.content_type = falcon.MEDIA_MSGPACK
    resp.status = falcon.HTTP_OK

class Film():

    def __init__(self, db):
        self._db = db
        self.log = logging.getLogger(__name__)

    # @falcon.after(set_content_type)
    def on_get(self, req, resp, index):
        try:
            index = int(index)
            film = self._db.film(index)
            resp.data = msgpack.dumps(film, use_bin_type=True)
            resp.content_type = falcon.MEDIA_MSGPACK
            resp.status = falcon.HTTP_OK
            self.log.debug('GET film %d', index)
        except (DatabaseError, ValueError):
            raise falcon.HTTPNotFound()
