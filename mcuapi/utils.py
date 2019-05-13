import falcon
import json
import logging
from functools import partial


MEDIA_HANDLERS = {
    'application/json': falcon.media.JSONHandler(dumps=partial(json.dumps, ensure_ascii=False)),
    'application/msgpack': falcon.media.MessagePackHandler()
}

def set_content_format(req, resp, resource, params):
    log = logging.getLogger(__name__)
    if 'format' in req.params and req.params['format'] == 'msgpack':
        resp.content_type = falcon.MEDIA_MSGPACK
        log.debug("req, format=msgpack")
    else:
        resp.content_type = falcon.MEDIA_JSON
        log.debug("req, format=json")

def set_content_formatter(req, resp, resource, params):
    pass
