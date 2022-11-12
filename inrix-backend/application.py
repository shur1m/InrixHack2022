from flask import Flask

from noiseApi import simple_page
from inrixAppAPIs import inrix_page

app = Flask(__name__)

app.register_blueprint(noise, "/noise")
app.register_blueprint(inrix_page, "/inrix")


@app.route("/")
def home():
    return "A group's Inrix API Hackathon Home Page"
