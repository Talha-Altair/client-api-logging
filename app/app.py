from flask import Flask, request, jsonify
import random
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

PORT = os.environ.get('PORT')

@app.route('/')
def index():

    headers = request.headers

    auth = headers.get("api_key")

    num = random.randint(1000,9999)

    data = {
       "number" : num
    }

    if auth == 'pass1':

        return jsonify({
           "message": "OK: Authorized Access to Client 1" ,
           "data":data
           }), 200
   
    if auth == 'pass2':

        return jsonify({
           "message": "OK: Authorized Access to Client 2" ,
           "data":data
           }), 200

    else:

        return jsonify({"message": "ERROR: Unauthorized"}), 401

if __name__ == '__main__':

    app.run(port = PORT)