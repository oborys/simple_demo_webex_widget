from flask import Flask
from flask import request
from flask import Flask, jsonify
from flask_cors import CORS
import base64
import requests
import time
import json
import math
import os
import configparser
import jwt


# read variables from config
credential = configparser.ConfigParser()
credential.read('webex_cred')
WEBEX_TEAMS_ISSUER_ID = credential['Webex']['WEBEX_TEAMS_ISSUER_ID']
WEBEX_TEAMS_ISSUER_SECRET = credential['Webex']['WEBEX_TEAMS_ISSUER_SECRET']

app = Flask(__name__)
#app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['POST'])
def createToken():
    data = request.get_json()
    print("data", data)
    expiration = math.floor(time.time()) + 3600 * int(data['tokenTime'])

    # Create a JWT payload object
    # 'sub' (subject) will be use to create the Webex Teams user email (sub@org-uuid)
    # 'name' will be the user's display name
    payload = {
        'sub': data['subject'],
        'name': data['name'],
        'iss': WEBEX_TEAMS_ISSUER_ID,
        'exp': expiration
        }

    # Base64 decode the Guest Issuer secret
    secret = base64.b64decode(WEBEX_TEAMS_ISSUER_SECRET)

    # Use the jwt library to encode, assemble and sign the JWT
    jwtToken = jwt.encode(payload, secret)

    # Use this token in application
    return(jwtToken.decode('utf-8'))


if __name__ == '__main__':
    app.run()
