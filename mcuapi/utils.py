import falcon
import json
import msgpack


def set_content_formatter(req, resp, resource, params):
    if 'format' in params and params['format'] == 'msgpack':
        def formatter(data):
            resp.content_type = falcon.MEDIA_MSGPACK
            resp.data = msgpack.dumps(data, use_bin_type=True)
    else:
        def formatter(data):
            resp.content_type = falcon.MEDIA_JSON
            resp.data = json.dumps(data), falcon.MEDIA_JSON

    resource.formatter = formatter

