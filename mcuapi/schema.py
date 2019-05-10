import msgpack
import falcon
import logging

from .utils import set_content_type

class FilmSchema():
    def __init__(self, db):
        self._db = db
        self.log = logging.getLogger(__name__)


    @falcon.after(set_content_type)
    def on_get(self, req, resp):
        resp.data = msgpack.dumps(self._db.film_schema, use_bin_type=True)
        self.log.debug('GET character schema')


class CharacterSchema():
    def __init__(self, db):
        self._db = db
        self.log = logging.getLogger(__name__)

    @falcon.after(set_content_type)
    def on_get(self, req, resp):
        resp.data = msgpack.dumps(self._db.character_schema, use_bin_type=True)
        self.log.debug('GET character schema')

