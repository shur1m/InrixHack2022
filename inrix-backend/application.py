from flask import Flask, jsonify, request
import json
import requests

from ApiWrappers.inrixAppAPIs import inrix_page
from ApiWrappers.weatherApi import weather_page
from ApiWrappers.inrixDistanceApi import inrix_distance
from ApiWrappers.bestTimeApi import besttime_page
from ApiWrappers.noiseApi import noise_page
from ApiWrappers.geocodeApi import geocode_page

app = Flask(__name__)

app.register_blueprint(inrix_page, url_prefix="/inrix")
app.register_blueprint(weather_page, url_prefix='/weather')
app.register_blueprint(inrix_distance, url_prefix='/route')
app.register_blueprint(besttime_page, url_prefix='/besttime')
app.register_blueprint(noise_page,url_prefix='/noise')
app.register_blueprint(geocode_page,url_prefix='/geocode')

@app.route("/")
def home():
    return "A group's Inrix API Hackathon Home Page"


# distance , travelTime, indor,outdoor,Location,address
@app.route("/places")
def places():
    with open("./ConfigFiles/locations.json", "r") as fp:
        res = json.loads(fp.read())

    return jsonify(res)






