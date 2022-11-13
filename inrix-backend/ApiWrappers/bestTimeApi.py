from flask import Blueprint, jsonify, request
import requests
import json

besttime_page = Blueprint('besttime_page', __name__)


@besttime_page.route("/")
def home():
    return "BestTime APIs for the Hackathon"


@besttime_page.route("/busyness")
def find_busyness():
    # Use app token for other requests
    name = request.args.get("name")
    address = request.args.get("address")
    url = "https://besttime.app/api/v1/forecasts"

    with open("./ConfigFiles/besttime.json", "r") as fp:
        api_keys = json.loads(fp.read())

    params = {
        'api_key_private': api_keys["api_key_private"],
        'venue_name': name,
        'venue_address': address
    }

    response = requests.post(url, params=params)
    return jsonify(response.json())
