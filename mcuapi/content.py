import falcon
import logging
import msgpack

from .utils import set_content_formatter
from .constants import MCUAPI_URL

class Content():
    _CONTENT = {
        "films": {
            "url": "/".join((MCUAPI_URL, 'films')),
            "description": "Films in the Marvel Cinematic Universe"
        },
        "characters": {
            "url": "/".join((MCUAPI_URL, 'characters')),
            "description": "Characters in the Marvel Cinematic Universe"
        }
    }


    def __init__(self):
        self._log = logging.getLogger(__name__)
        self.formatter = None


    @falcon.before(set_content_formatter)
    def on_get(self, req, resp):
        self.formatter(self._CONTENT)
        self._log.info("GET Contents")

