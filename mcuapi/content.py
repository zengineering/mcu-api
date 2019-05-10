import falcon
import logging
import msgpack

from .utils import set_content_type
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


    @falcon.after(set_content_type)
    def on_get(self, req, resp):
        resp.data = msgpack.dumps(self._CONTENT, use_bin_type=True)
        self._log.info("GET Contents")

