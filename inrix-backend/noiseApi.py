from flask import Blueprint


simple_page = Blueprint('simple_page', __name__)

@simple_page.route('/page')
def show():
    return "Hellow World"