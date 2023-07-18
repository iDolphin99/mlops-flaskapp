from flask import Flask
from flask import request

import requests
import re
import socket

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Flask!'
