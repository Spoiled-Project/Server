from flask import Flask, request
from flask_cors import CORS
import os

"""
from Handler import handle_req
from utils import *
from Validator import return_errors
"""


app = Flask(__name__)
CORS(app)


@app.route('/', endpoint='index', methods=['GET'])
#@return_errors
def index():
    return "hello"


@app.route('/', endpoint='check', methods=['POST'])
#@return_errors
def check():
    return "world"


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 8080)), host='0.0.0.0',debug=True)
