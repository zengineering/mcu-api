import msgpack
import falcon
import logging

from .utils import set_content_format

class FilmSchema():
    def __init__(self, db):
        self._db = db
        self._log = logging.getLogger(__name__)
        self.format = None


    @falcon.before(set_content_format)
    def on_get(self, req, resp):
        resp.media = self._db.film_schema
        self._log.debug('GET character schema')


class CharacterSchema():
    def __init__(self, db):
        self._db = db
        self._log = logging.getLogger(__name__)

    @falcon.before(set_content_format)
    def on_get(self, req, resp):
        resp.media = self._db.character_schema
        self._log.debug('GET character schema')

