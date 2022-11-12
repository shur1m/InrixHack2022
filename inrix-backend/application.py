from flask import Flask

from noiseApi import noise
from inrixAppAPIs import inrix_page

app = Flask(__name__)

app.register_blueprint(noise, url_prefix="/noise")
app.register_blueprint(inrix_page, url_prefix="/inrix")


@app.route("/")
def home():
    return "A group's Inrix API Hackathon Home Page"
