import json
import pathlib
import logging

log = logging.getLogger(__name__)

class Database():
    _DATA_PATH = pathlib.Path(__file__).parent.resolve() / 'data'
    _CHARACTERS_FILE = 'characters.json'
    _FILMS_FILE = 'films.json'

    def __init__(self):
        with open(self._DATA_PATH / self._CHARACTERS_FILE, 'r') as f:
            self._characters = json.load(f)
        with open(self._DATA_PATH / self._FILMS_FILE, 'r') as f:
            self._films = json.load(f)

    def character(self, index):
        try:
            char = self._characters[index]
        except IndexError:
            raise DatabaseError("No character with index '{}'".format(index))
        else:
           return char

    def film(self, index):
        try:
            film = self._films[index]
        except IndexError:
            msg = "No film with index '{}'".format(index)
            log.error(msg)
            raise DatabaseError(msg)
        else:
           return film
