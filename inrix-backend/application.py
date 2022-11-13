from flask import Flask, jsonify
import json

from ApiWrappers.inrixAppAPIs import inrix_page
from ApiWrappers.weatherApi import weather
from ApiWrappers.inrixDistanceApi import inrix_distance
from ApiWrappers.bestTimeApi import besttime_page

app = Flask(__name__)

app.register_blueprint(inrix_page, url_prefix="/inrix")
app.register_blueprint(weather, url_prefix='/weather')
app.register_blueprint(inrix_distance, url_prefix='/route')
app.register_blueprint(besttime_page, url_prefix='/besttime')


@app.route("/")
def home():
    return "A group's Inrix API Hackathon Home Page"


@app.route("/places")
def places():
    with open("./ConfigFiles/locations.json", "r") as fp:
        res = json.loads(fp.read())

    return jsonify(res)
