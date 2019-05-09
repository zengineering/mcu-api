import falcon
import logging
import json
import msgpack
from .errors import DatabaseError
from .utils import set_content_type


class Film():
    def __init__(self, db):
        self._db = db
        self.log = logging.getLogger(__name__)

    @falcon.after(set_content_type)
    def on_get(self, req, resp, index=None):
        if index is not None:
            self.get_film(req, resp, index)
        else:
            resp.data = msgpack.dumps(self._db.films(), use_bin_type=True)
            self.log.debug('GET film list')

    @falcon.after(set_content_type)
    def get_film(self, req, resp, index):
        try:
            film = self._db.film(index)
            resp.data = msgpack.dumps(film, use_bin_type=True)
            self.log.debug('GET film %d', index)
        except (DatabaseError, ValueError):
            raise falcon.HTTPNotFound()
