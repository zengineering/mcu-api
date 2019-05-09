import falcon
import logging
from mcuapi.films import Film
from mcuapi.characters import Character
from mcuapi.database import Database

logging.basicConfig(filename='mcuapi.log',
                    format='[%(asctime)s] (%(levelname)s) %(module)s.%(funcName)s: %(message)s',
                    level=logging.DEBUG)

def create_app(db):
    api = falcon.API()
    api.add_route('/films', Film(db))
    api.add_route('/films/{index:int}', Film(db))
    api.add_route('/characters', Character(db))
    api.add_route('/characters/{index:int}', Character(db))
    return api

def get_app():
    db = Database()
    return create_app(db)
