from Handler import handle_req
from flask import Flask, request
from flask_cors import CORS
from utils import *
from Validator import return_errors
from os import environ

app = Flask(__name__)
CORS(app)


@app.route('/', endpoint='index', methods=['GET'])
@return_errors
def index():
    return get_ser_lst()


@app.route('/', endpoint='check', methods=['POST'])
@return_errors
def check():
    return handle_req(request.get_json())


if __name__ == '__main__':
    app.run(port=int(environ.get("PORT", 8080)), host='0.0.0.0',debug=True)
