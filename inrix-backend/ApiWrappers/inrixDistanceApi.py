from flask import Blueprint, request, jsonify
from inrix_requests import InrixAPI
import time
inrix_requests = InrixAPI()

inrix_distance = Blueprint('inrix_distance', __name__)


def handle_dist_time_req(wp_1lat, wp_1long, wp_2lat, wp_2long):
    params = {
        "format": "json",
        "wp_1": f'{wp_1lat},{wp_1long}',
        "wp_2": f'{wp_2lat},{wp_2long}'}
    find_routes = inrix_requests.get("https://api.iq.inrix.com/findRoute", params)
    print(find_routes)
    time.sleep(.7)
    return {
        "travelTime": find_routes.get('result').get('trip').get("routes")[0].get('totalDistance'),
        "totalDistance": find_routes.get('result').get('trip').get("routes")[0].get('travelTimeMinutes')
    }


@inrix_distance.route('/distancetime')
def get_distance_and_travel_time():
    return jsonify(handle_dist_time_req(
        request.args.get("wp_1lat"), request.args.get("wp_1long"),
        request.args.get("wp_2lat"), request.args.get("wp_2long")
    ))



# ?wp_1=37.770581%2C-122.442550&wp_2=37.765297%2C-122.442527&format=json
@inrix_distance.route('/route')
def get_route():
    params = {
        "format": "json",
        "wp_1": f'{request.args.get("wp_1lat")},{request.args.get("wp_1long")}',
        "wp_2": f'{request.args.get("wp_2lat")},{request.args.get("wp_2long")}'
    }

    find_routes = inrix_requests.get("https://api.iq.inrix.com/findRoute", params)

    tripid = find_routes.get('result').get('trip').get('tripId')
    params = {
        "routeId": int(tripid),
        "format": "json",
        "routeOutputFields": "D,S,W,B,I,U,P"
    }

    route = inrix_requests.get("https://api.iq.inrix.com/route", params)
    return jsonify(route.get('result').get('trip').get('routes')[0].get('points').get('coordinates'))
    