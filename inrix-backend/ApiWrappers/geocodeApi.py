from flask import Flask, jsonify, request, Blueprint
import json
import requests



geocode_page =Blueprint('geocode',__name__)


@geocode_page.route("/txtToPoint")
def address_to_point():
    address = request.args.get("searchText")
    with open("./ConfigFiles/ptv.json", "r") as fp:
        res = json.loads(fp.read())

    params = {"apiKey": res["apikey"], "searchText": address}

    url = "https://api.myptv.com/geocoding/v1/locations/by-text"

    result = requests.get(url, params=params)
    if len(result.json()['locations']) == 0:
        return jsonify("No Result")

    return jsonify(result.json()['locations'][:10])