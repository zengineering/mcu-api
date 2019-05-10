import falcon
import logging
import json
import msgpack
from .errors import DatabaseError
from .utils import set_content_type

class Character():
    def __init__(self, db):
        self._db = db
        self.log = logging.getLogger(__name__)


    @falcon.after(set_content_type)
    def on_get(self, req, resp, index=None):
        if index is not None:
            self.get_character(req, resp, index)
        else:
            resp.data = msgpack.dumps(self._db.characters, use_bin_type=True)
            self.log.debug('GET character list')


    @falcon.after(set_content_type)
    def get_character(self, req, resp, index):
        try:
            character = self._db.character(index)
            resp.data = msgpack.dumps(character, use_bin_type=True)
            self.log.debug('GET character %d', index)
        except (DatabaseError, ValueError):
            raise falcon.HTTPNotFound()

