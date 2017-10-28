import os
import sys
import json
from datetime import datetime

import requests
from flask import Flask, request

app = Flask(__name__)

def log(msg, *args, **kwargs):  # simple wrapper for logging to stdout on heroku
    try:
        if type(msg) is dict:
            msg = json.dumps(msg)
        else:
            msg = msg.format(*args, **kwargs)
        print(u"{}: {}".format(datetime.now(), msg))
    except UnicodeEncodeError:
        pass  # squash logging errors in case of non-ascii text
    sys.stdout.flush()

@app.route('/', methods=['GET'])
def verify():
    return "Hello world", 200

def valid(data):
    required_keys = ['song_id', 'user_id']
    if not all(key in data for key in required_keys):
        return False

    if len(data) != len(required_keys):
        return False
    return True

@app.route('/', methods=['POST'])
def webhook():

    # endpoint for processing incoming messaging events

    data = request.get_json()
    log(data)  # you may not want to log every incoming message in production, but it's good for testing
    if not valid(data):
        return "Malformed request", 400

    return "ok", 200



if __name__ == '__main__':
    app.run(debug=True)
