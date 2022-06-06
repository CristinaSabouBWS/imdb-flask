from imdb_flask import ROOT_PATH
import os
import json

JSON_URL = os.path.join(ROOT_PATH, "src/imdb_flask/static", "imdb_movie.json")


class Movie:
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @classmethod
    def all(cls):
        all_movies = []
        with open(JSON_URL) as f:
            for jsonObj in f:
                movieDict = json.loads(jsonObj)
                movie = Movie(**movieDict)
                all_movies.append(movie)
        return all_movies

    def to_json(self):
        return dict(title=self.title, genres=self.genres)

    @classmethod
    def first(cls):
        return cls.all()[0]
