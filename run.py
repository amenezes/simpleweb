import json

from config import CF

from flask import Flask, escape, request


cf = CF()
cf.get_config()

app = Flask(__name__)


@app.route('/')
def hello():
    return f"Welcome to <b>simpleweb000</b>"


@app.route('/config')
def config():
    return cf.config


@app.route('/config-keys')
def keys():
    return json.dumps(list(cf.get_keys()))
