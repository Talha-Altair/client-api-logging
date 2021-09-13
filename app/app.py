from flask import Flask, request, jsonify
import random
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

PORT = os.environ.get('PORT')

@app.route('/', methods = ['POST','GET'])
def index():

    headers = request.headers

    auth = headers.get("api_key")

    num = random.randint(1000,9999)

    data = {
       "number" : num
    }

    if auth == 'pass1':

        response_data = {
           "message": "OK: Authorized Access to Client 1" ,
           "data":data
           }

        app.logger.info(response_data)

        return jsonify(response_data), 200
   
    if auth == 'pass2':

        response_data = {
           "message": "OK: Authorized Access to Client 2" ,
           "data":data
           }

        app.logger.info(response_data)

        return jsonify(response_data), 200

    else:

        response_data = {"message": "ERROR: Unauthorized"}

        app.logger.info(response_data)

        return jsonify(response_data), 401

if __name__ == '__main__':

    app.run(debug = True, port = PORT)