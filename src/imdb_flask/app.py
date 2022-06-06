from flask import Flask, render_template
import json
import os
import ipdb
from imdb_flask.configuration import config

app = Flask(__name__, template_folder="static")
# app.config.update(config().as_dict())
from imdb_flask.controllers.movies import movies_blueprint

app.register_blueprint(movies_blueprint)
