import json
import pathlib
import logging
from urllib.parse import urljoin
from .errors import DatabaseError
from .constants import MCUAPI_URL

class Database():
    _DATA_PATH = pathlib.Path(__file__).parent.resolve() / 'data'
    _CHARACTERS_FILE = 'characters.json'
    _FILMS_FILE = 'films.json'
    _FILM_SCHEMA_FILE = 'film_schema.json'
    _CHARACTER_SCHEMA_FILE = 'character_schema.json'


    def __init__(self):
        self.log = logging.getLogger(__name__)
        with open(self._DATA_PATH / self._CHARACTERS_FILE, 'r') as f:
            self._characters = json.load(f)
        with open(self._DATA_PATH / self._FILMS_FILE, 'r') as f:
            self._films = json.load(f)
        with open(self._DATA_PATH / self._CHARACTER_SCHEMA_FILE, 'r') as f:
            self._character_schema = json.load(f)
            self._character_schema['$id'] = '/'.join((MCUAPI_URL, 'characters', 'schema'))
        with open(self._DATA_PATH / self._FILM_SCHEMA_FILE, 'r') as f:
            self._film_schema = json.load(f)
            self._film_schema['$id'] = '/'.join((MCUAPI_URL, 'films', 'schema'))


    def character(self, index):
        try:
            char = self._characters[index-1]
        except IndexError:
            msg = "No character with index '%d'"
            self.log.error(msg, index)
            raise DatabaseError(msg.format(index))
        else:
            self.log.debug("character lookup: %d", index)
            return char


    @property
    def characters(self):
        return ['/'.join((MCUAPI_URL, 'characters', str(i)))
                for i in range(1, len(self._characters)+1)]


    @property
    def character_count(self):
        return len(self._characters)


    @property
    def character_schema(self):
        return self._character_schema


    def film(self, index):
        try:
            film = self._films[index-1]
        except IndexError:
            msg = "No film with index '%d'"
            self.log.error(msg, index)
            raise DatabaseError(msg.format(index))
        else:
            self.log.debug("film lookup: %d", index)
            return film


    @property
    def films(self):
        return ['/'.join((MCUAPI_URL, 'films', str(i)))
                for i in range(1, len(self._films)+1)]


    @property
    def film_count(self):
        return len(self._films)


    @property
    def film_schema(self):
        return self._film_schema
