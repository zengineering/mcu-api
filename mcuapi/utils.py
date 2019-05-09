import falcon

def set_content_type(req, resp, resource):
    resp.content_type = falcon.MEDIA_MSGPACK
    resp.status = falcon.HTTP_OK
