import msgpack
import falcon
import logging

from .utils import set_content_formatter

class FilmSchema():
    def __init__(self, db):
        self._db = db
        self._log = logging.getLogger(__name__)
        self.formatter = None


    @falcon.before(set_content_formatter)
    def on_get(self, req, resp):
        resp.data = msgpack.dumps(self._db.film_schema, use_bin_type=True)
        self._log.debug('GET character schema')


class CharacterSchema():
    def __init__(self, db):
        self._db = db
        self._log = logging.getLogger(__name__)

    @falcon.before(set_content_formatter)
    def on_get(self, req, resp):
        resp.data = msgpack.dumps(self._db.character_schema, use_bin_type=True)
        self._log.debug('GET character schema')

