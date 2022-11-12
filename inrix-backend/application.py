from inrix_requests import InrixAPI
from flask import Flask, jsonify, request

from noiseApi import simple_page

app = Flask(__name__)
inrix_requests = InrixAPI()

app.register_blueprint(simple_page,"/page")


@app.route("/")
def home():
    return "A group's Inrix API Hackathon Home Page"


@app.route("/lots")
def find_lots():
    # Use app token for other requests
    latitude = request.args.get("lat")
    longitude = request.args.get("long")
    radius = request.args.get("radius", "300")

    # Ex: https://api.iq.inrix.com/lots/v3?point=37.74638779388551|-122.42209196090698&radius=300
    params = {"point": f"{latitude}|{longitude}", "radius": radius}
    url = 'https://api.iq.inrix.com/lots/v3'
    res = inrix_requests.get(url, params)

    return jsonify(res)
