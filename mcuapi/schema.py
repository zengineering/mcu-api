from .constants import MCUAPI_URL
class FilmSchema():
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "/".join((MCUAPI_URL, 'films', 'schema')),
        "title": "Film",
        "description": "A film in the Marvel Cinematic Universe",
        "type": "object",
        "properties": {
            "title": {
                "type": "string",
                "description": "The title of the film"
            },
            "release": {
                "type": "string",
                "description": "The date of the films theatrical release"
            },
            "director": {
                "type": "string",
                "description": "The name(s) of the film's director(s)"
            }
            "id": {
                "type": "integer",
                "description": "The unique identifier/index of the film"
            }
            "runtime": {
                "type": "integer",
                "description": "The runtime of the film in minutes"
            },
            "box-office-usa": {
                "type": "number",
                "description": "The USA box office revenue produced by the film"
            }
            "box-office-world": {
                "type": "number",
                "description": "The international box office revenue produced by the film"
            }
            "rotten-tomatoes-critic": {
                "type": "integer",
                "description": "The Rotten Tomatoes critic review average (tomatometer)"
            },
            "rotten-tomatoes-audience": {
                "type": "integer",
                "description": "The Rotten Tomatoes average audence score"
            }
        },
        "required": [
            "title",
            "release",
            "director",
            "id",
            "runtime",
            "box-office-usa",
            "box-office-world",
            "rotten-tomatoes-critic",
            "rotten-tomatoes-audience",
        ]
    }

    def on_get(self, req, resp):
        pass


class CharacterSchema():
    SCHEMA = {
        "$schema": "http://json-schema.org/draft-07/schema#",
        "$id": "/".join((MCUAPI_URL, 'characters', 'schema')),
        "title": "Film",
        "description": "A character in the Marvel Cinematic Universe",
        "type": "object",
        "properties": {
            "name": {
                "type": "string",
                "description": "The name of the character"
            }
            "alter-ego": {
                "type": "string",
                "description": "The alternate/superhero name of the character"
            },
            "actors": {
                "type": "array",
                "description": "The actor(s) that have portrayed the character"
                "items": {
                    "type": "string"
                },
            },
            "id": {
                "type": "integer",
                "description": "The unique identifier/index of the film"
            }
            "films" : {
                "type": "array",
                "description": "The id's of the films in which the character has appeared"
                "items": {
                    "type": "integer"
                }
            }
        },
        "required": [
            "name",
            "alter-ego",
            "actors",
            "id",
            "films"
        ]
    }
    def on_get(self, req, resp):
        pass
