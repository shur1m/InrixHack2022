from flask import Blueprint, request,jsonify
import requests


weather_page = Blueprint('weather', __name__)
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

def handle_weather_req(longitude, latitude):
    params = dict()
    params['longitude'] = longitude
    params['latitude'] = latitude
    params["current_weather"] = True
    params["temperature_unit"] = "fahrenheit"
    result = requests.get('https://api.open-meteo.com/v1/forecast', params).json()
    result["current_weather"]["weathercode"] = WMO[result["current_weather"]["weathercode"]]
    return result


@weather_page.route('/weather')
def get_weather():
    # https://api.open-meteo.com/v1/forecast?latitude=55.6763&longitude=12.5681&hourly=temperature_2m
    result = handle_weather_req(request.args.get('long'), request.args.get('lat'))
    return jsonify(result)
