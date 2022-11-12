from flask import Blueprint, jsonify, request
from inrix_requests import InrixAPI
inrix_requests = InrixAPI()

inrix_page = Blueprint('inrix_page', __name__)


@inrix_page.route("/")
def home():
    return "Inrix APIs for the Hackathon"


@inrix_page.route("/lots")
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
