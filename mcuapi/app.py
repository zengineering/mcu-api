import os
import falcon
from mcuapi.films import Film
from mcuapi.database import Database

def create_app(db):
    api = falcon.API()
    api.add_route('/film/{index}', Film(db))
    return api

def get_app():
    db = Database()
    return create_app(db)
