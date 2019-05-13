import falcon
import logging
import msgpack

from .utils import set_content_format
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


    @falcon.before(set_content_format)
    def on_get(self, req, resp):
        resp.media = self._CONTENT
        self._log.info("GET Contents")

