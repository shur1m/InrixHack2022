from flask import Blueprint
import requests


weather = Blueprint('weather', __name__)

@weather.route('/weather')
def getWeather():
    #https://api.open-meteo.com/v1/forecast?latitude=55.6763&longitude=12.5681&hourly=temperature_2m
    params=dict()
    params['longitude']=requests.args.get('lon')
    params['latitude']=requests.args.get('lat')
    params['hourly']='temperature_2m'
    query=requests.get(f'https://api.open-meteo.com/v1/forecast', params=params)
    
    return query