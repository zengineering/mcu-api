import falcon
import logging
import json
import msgpack
from .errors import DatabaseError
from .utils import set_content_format

class Film():
    def __init__(self, db):
        self._db = db
        self.log = logging.getLogger(__name__)
        self.format = None


    @falcon.before(set_content_format)
    def on_get(self, req, resp, index=None):
        if index is not None:
            self.get_film(req, resp, index)
        else:
            resp.media = self._db.films
            self.log.debug('GET film list')


    def get_film(self, req, resp, index):
        try:
            film = self._db.film(index)
            resp.media = film
            self.log.debug('GET film %d', index)
        except (DatabaseError, ValueError):
            raise falcon.HTTPNotFound()
