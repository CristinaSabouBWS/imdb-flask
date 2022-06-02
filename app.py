from flask import Flask, render_template
import json
import os

app = Flask(__name__)


# def validate_input(number):
#     return number != 0


@app.route("/movies")
def movie_page():
    fileData = 0
    fileData = []
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "media", "imdb_movie.json")
    with open(json_url) as f:
        for jsonObj in f:
            movieDict = json.loads(jsonObj)
            fileData.append(movieDict)
    f.close()

    line = fileData[0]
    imaages = line["images"]
    first_item_images = imaages[0]
    image_url = os.path.join(SITE_ROOT, "media/images_file", first_item_images["path"])
    print(image_url)
    return render_template("index.html", fileData=fileData)
