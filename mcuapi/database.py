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


    def __init__(self):
        self.log = logging.getLogger(__name__)
        with open(self._DATA_PATH / self._CHARACTERS_FILE, 'r') as f:
            self._characters = json.load(f)
        with open(self._DATA_PATH / self._FILMS_FILE, 'r') as f:
            self._films = json.load(f)


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


    def films(self):
        return ['/'.join((MCUAPI_URL, 'films', str(i))) for i in range(1, len(self._films)+1)]


    def characters(self):
        return ['/'.join((MCUAPI_URL, 'characters', str(i))) for i in range(1, len(self._films)+1)]


    def character_count(self):
        return len(self._characters)


    def film_count(self):
        return len(self._films)
