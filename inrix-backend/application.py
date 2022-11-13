from flask import Flask, jsonify, request
import json
import requests
import asyncio
import aiohttp

from ApiWrappers.inrixAppAPIs import inrix_page
from ApiWrappers.weatherApi import weather_page, handle_weather_req
from ApiWrappers.inrixDistanceApi import inrix_distance, handle_dist_time_req
from ApiWrappers.bestTimeApi import besttime_page
from ApiWrappers.noiseApi import noise_page, handle_noise_req
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
    distance_thres=request.args.get("distance")
    time_thres=request.args.get("time")
    indoor=bool(request.args.get("indoor"))
    noise_thres=float(request.args.get("noise"))

    with open("./ConfigFiles/locations.json", "r") as fp:
        res = json.loads(fp.read())

    weather = []
    noise = []
    distance = []
    time = []
    busyness = []
    

    #prunes out locations based on outdoor cs indoor
    for i in range(len(res)):
        if indoor and not res[i]["Indoor"]:
            res[i]=None
    #prunes out be distance
    for i in range(len(res)):
        if not res[i]:
            continue

        # Calculates the distance and time
        distancetime_result = handle_dist_time_req(lat, lon, res[i]["Latitude"], res[i]["Longitude"])
        distance.append((distancetime_result["totalDistance"], i))
        if float(distancetime_result["totalDistance"]) > float(distance_thres):
            res[i]=None
            continue
        time.append((distancetime_result["travelTime"], i))
        if float(distancetime_result["travelTime"]) > float(time_thres):
            res[i]=None
            continue
        res[i]["travelTime"]=distancetime_result["travelTime"]
        res[i]["totalDistance"]=distancetime_result["totalDistance"]
    

    


    #for i in range(len(res)):
    #    if not res[i]:
    #        continue
        # busyness_result = await fetch(HOME_URL+routes[4],{"name":res[i]["Name"],"address":res[i]["Address"]})
    #    busyness.append((res[i]["Busyness"], i))
    for i in range(len(res)):
        if not res[i]:
            continue
        noise_result = handle_noise_req(res[i]["Latitude"], res[i]["Longitude"])
        if float(noise_result[0]['score']) > noise_thres:
            res[i]=None
            continue
        noise.append((noise_result[0]['score'], i))
        res[i]["NoiseScore"]=noise_result[0]['score']
    for i in range(len(res)):
        if not res[i]:
            continue
        # Calculates weather score

        # Calculates weather score
        weather_result = handle_weather_req(res[i]["Longitude"], res[i]["Latitude"])
        weather.append((abs(weather_result["current_weather"]["temperature"] - 70), i))

                        
        

    

        

    

    score=[[0,i] for i in range(len(res))]
    time=[(float(x[0]),x[1]) for x in time]

    weather.sort()
    noise.sort()
    distance.sort()
    time.sort()
    busyness.sort()
    
    #calculate remote 
    for i in range(len(time)):
        score[time[i][1]][0]+=i
    for i in range(len(distance)):
        score[distance[i][1]][0]+=i
    for i in range(len(weather)):
        score[weather[i][1]][0]+=i
    for i in range(len(busyness)):
        score[busyness[i][1]][0]+=i
    for i in range(len(noise)):
        score[noise[i][1]][0]+=i

    score.sort()

    
    for i in range(len(score)):
        if not res[score[i][1]] :
            continue
        res[score[i][1]]["Score"]=score[i][0]

    
    while(None in res):
        res.remove(None)


    return res
    
        





