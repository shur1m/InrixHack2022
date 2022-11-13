from flask import Flask, jsonify, request
import json
import requests

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

#distance , travelTime, indor,outdoor,Location,address
@app.route("/places")
def places():
    with open("./ConfigFiles/locations.json", "r") as fp:
        res = json.loads(fp.read())

    return jsonify(res)


#\d{1,5}\s\w.\s(\b\w*\b\s){1,2}\w*\.
@app.route("/txtToPoint")
def addressToPoint():
    address=request.args.get("searchText")
    with open("./ConfigFiles/ptv.json", "r") as fp:
        res = json.loads(fp.read())

    params={"apiKey":res["apikey"],"searchText": address}

    url="https://api.myptv.com/geocoding/v1/locations/by-text"

    result=requests.get(url,params=params)
    if (len(result.json()['locations'])==0):
        return jsonify("No Result")
    l=min(len(result.json()['locations']),10)
    return jsonify(result.json()['locations'][:l])