import falcon
import json
import msgpack
import logging


def set_content_formatter(req, resp, resource, params):
    log = logging.getLogger(__name__)
    if 'format' in req.params and req.params['format'] == 'json':
        def formatter(data):
            resp.body = json.dumps(data, ensure_ascii=False)
            resp.content_type = falcon.MEDIA_JSON
    else:
        def formatter(data):
            resp.data = msgpack.dumps(data, use_bin_type=True)
            resp.content_Type = falcon.MEDIA_MSGPACK

    resource.formatter = formatter

