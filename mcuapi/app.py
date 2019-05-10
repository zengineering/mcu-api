import falcon
import logging
from mcuapi.films import Film
from mcuapi.characters import Character
from mcuapi.database import Database
from mcuapi.schema import FilmSchema, CharacterSchema

logging.basicConfig(filename='mcuapi.log',
                    format='[%(asctime)s] (%(levelname)s) %(module)s.%(funcName)s: %(message)s',
                    level=logging.DEBUG)

def create_app(db):
    api = falcon.API()
    api.add_route('/api/films', Film(db))
    api.add_route('/api/films/{index:int}', Film(db))
    api.add_route('/api/films/schema', FilmSchema(db))
    api.add_route('/api/characters', Character(db))
    api.add_route('/api/characters/{index:int}', Character(db))
    api.add_route('/api/characters/schema', CharacterSchema(db))
    return api

def get_app():
    db = Database()
    return create_app(db)
