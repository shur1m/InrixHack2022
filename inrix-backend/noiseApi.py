from flask import Blueprint


noise = Blueprint('noise', __name__)

@noise.route('/noise')
def show():
    return "Hellow World"