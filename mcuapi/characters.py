import falcon
import logging
import json
import msgpack
from .errors import DatabaseError
from .utils import set_content_format


class Character():
    def __init__(self, db):
        self._db = db
        self.log = logging.getLogger(__name__)
        self.format = None


    @falcon.before(set_content_format)
    def on_get(self, req, resp, index=None):
        if index is not None:
            self.get_character(req, resp, index)
        else:
            resp.media = self._db.characters
            self.log.debug('GET character list')


    def get_character(self, req, resp, index):
        try:
            character = self._db.character(index)
            resp.media = character
            self.log.debug('GET character %d', index)
        except (DatabaseError, ValueError):
            raise falcon.HTTPNotFound()

