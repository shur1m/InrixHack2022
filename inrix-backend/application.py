from flask import Flask, jsonify, request
import json
import requests
import asyncio
import aiohttp

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
app.register_blueprint(noise_page, url_prefix='/noise')
app.register_blueprint(geocode_page, url_prefix='/geocode')


async def fetch(url, params):
    async with aiohttp.request('GET', url, params=params) as resp:
        assert resp.status == 200
        data = await resp.read()
        return json.loads(data)


@app.route("/")
def home():
    return "A group's Inrix API Hackathon Home Page"


routes = ["/gecode/txtToPoint", "/weather/weather", "/route/distancetime", "/noise/getnoise", "/besttime/busyness"]
HOME_URL = "https://inrix-hack-api.herokuapp.com/"


# distance , travelTime, indor,outdoor,Location,address,noise
@app.route("/places")
async def places():
    lat = request.args.get("lat")
    lon = request.args.get("long")
    with open("./ConfigFiles/locations.json", "r") as fp:
        res = json.loads(fp.read())

    weather = []
    noise = []
    distance = []
    time = []
    busyness = []
    indoor = []

    for i in range(len(res)):
        # Calculates weather score
        weather_result = await fetch(HOME_URL + routes[1],
                                     params={"lat": res[i]["Latitude"], "long": res[i]["Longitude"]})
        weather.append((abs(weather_result["current_weather"]["temperature"] - 70), i))

        # Calculates the distance and time
        distancetime_result = await fetch(HOME_URL + routes[2],
                                          params={"wp_1lat": lat, "wp_1long": lon, "wp_2lat": res[i]["Latitude"],
                                                  "wp_2long": res[i]["Longitude"]})
        distance.append((distancetime_result["totalDistance"], i))
        time.append((distancetime_result["travelTime"], i))

        # busyness_result = await fetch(HOME_URL+routes[4],{"name":res[i]["Name"],"address":res[i]["Address"]})
        busyness.append((res[i]["Busyness"], i))

        noise_result = await fetch(HOME_URL + routes[3],
                                   params={"lat": res[i]["Latitude"], "long": res[i]["Longitude"]})
        noise.append((noise_result[0]['score'], i))

    return "Hello"





