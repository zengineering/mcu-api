import falcon
from .errors import DatabaseError

def set_content_type(req, resp, resource, params):
    resp.content_type = 'application/json'

class Film():

    def __init__(self, db):
        self._db = db

    @falcon.after(set_content_type)
    def on_get(self, req, resp, index):
        try:
            film = self._db.film(index)
            doc = json.dumps(film)
            resp.data = msgpack.packb(doc, use_bin_type=True)
        except DatabaseError:
            raise falcon.HTTPNotFound()
