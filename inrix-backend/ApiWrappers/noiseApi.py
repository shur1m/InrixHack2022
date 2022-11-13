from flask import Flask, jsonify, request, Blueprint
import json
import requests


noise_page = Blueprint('noise',__name__)

def handle_noise_req(latitude, longitude):
    params={"lng": longitude,"lat": latitude}
    url = 'https://api.howloud.com/score'
    
    with open("./ConfigFiles/howloud.json", "r") as fp:
        api_key = json.loads(fp.read())['apiKey']
    headers = {'x-api-key':api_key}
    result = requests.get(url, params=params, headers=headers)
    return result.json()['result']


@noise_page.route('/getnoise')
def get_noise_level():
    res = handle_noise_req(request.args.get("lat"), request.args.get("long"))
    return jsonify(res)
