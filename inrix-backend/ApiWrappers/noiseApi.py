from flask import Flask, jsonify, request, Blueprint
import json
import requests



noise_page =Blueprint('noise',__name__)


@noise_page.route('/getnoise')
def get_noise_level():
    params={"lng":request.args.get("long"),"lat":request.args.get("lat")}
    url = 'https://api.howloud.com/score'
    
    with open("./ConfigFiles/howloud.json", "r") as fp:
        api_key = json.loads(fp.read())['apiKey']
    headers = {'x-api-key':api_key}
    result = requests.get(url, params=params, headers=headers)
    return result.json()['result']