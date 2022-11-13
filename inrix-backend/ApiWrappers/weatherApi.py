from flask import Blueprint, request,jsonify
import requests


weather = Blueprint('weather', __name__)
WMO = {
    0: "Clear Sky",
    1: "Mainly Clear",
    2: "Partly Cloudly",
    3: "Overcast",
    45: "Fog",
    48: "Depositing Rime Fog",
    51: "Light Drizzle",
    53: "Moderate Drizzle",
    54: "Dense Drizzle",
    56: "Freezing Drizzle",
    57: "Freezing Drizzle",
    61: "Rain",
    63: "Rain",
    65: "Rain",
    66: "Rain",
    67: "Rain"
}


@weather.route('/weather')
def get_weather():
    # https://api.open-meteo.com/v1/forecast?latitude=55.6763&longitude=12.5681&hourly=temperature_2m
    params = dict()
    params['longitude'] = request.args.get('lon')
    params['latitude'] = request.args.get('lat')
    params["current_weather"] = True
    params["temperature_unit"] = "Fahrenheit"
    result = requests.get('https://api.open-meteo.com/v1/forecast', params).json()
    result["current_weather"]["weathercode"] = WMO[result["current_weather"]["weathercode"]]

    return jsonify(result)
