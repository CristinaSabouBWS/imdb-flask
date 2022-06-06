from flask import Flask, Blueprint, jsonify, render_template
import os
import json
from imdb_flask import ROOT_PATH
from imdb_flask.models.movie import Movie

movies_blueprint = Blueprint("movies", __name__)


@movies_blueprint.route("/movies")
def index():
    all_movies = Movie.all()
    import ipdb

    ipdb.set_trace()

    for line in fileData:
        count += 1
        imaages = line["images"]
        images_urls = line["image_urls"]
        if len(imaages) > 0:
            first_item_images = imaages[0]
            image_url = "media/images_file/" + first_item_images["path"]
            line["images"] = image_url
            first_item_image_url = images_urls[0]
            line["image_urls"] = first_item_image_url
            fileData[count] = line

    return render_template("templates/movies/index.html", fileData=fileData)
