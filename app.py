from Handler import handle_req
from flask import Flask, request
from flask_cors import CORS
from utils import *
from Validator import return_errors
from os import environ
from Macros.RestsMacros import SERIES, IMAGES

app = Flask(__name__)
CORS(app)

@app.route('/', endpoint='index', methods=['GET'])
@return_errors
def index():
    """
    The function receives all the get requests to the server's root, and returns a list of all the supported series
    by the server.
    """
    return get_ser_lst()


@app.route('/', endpoint='check', methods=['POST'])
@return_errors
def check():
    f"""
    The function receives a POST request which contains in its body the parameters:
    {SERIES} : Array which contains strings of the series wanted to be detected.
    {IMAGES} : Array of images' urls need to be checked.
    The function returns an json that each image's url is a key and each value is if the key's url is detected as one
    of the received series' spoiler or not.
    """
    return handle_req(request.get_json())


if __name__ == '__main__':
    from Series.SerieDetector.models import model
    model_instance = model
    app.run(port=int(environ.get("PORT", 8080)), host='0.0.0.0')
