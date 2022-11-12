from flask import Flask

from noiseApi import noise
from inrixAppAPIs import inrix_page
from weatherApi import weather

app = Flask(__name__)

app.register_blueprint(noise, url_prefix="/noise")
app.register_blueprint(inrix_page, url_prefix="/inrix")
app.register_blueprint(weather,url_prefix='/weather')


@app.route("/")
def home():
    return "A group's Inrix API Hackathon Home Page"
