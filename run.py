import json

from config.cf import CF

from flask import Flask, escape, request


cf = CF()
cf.get_config()

app = Flask(__name__)


@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/config')
def config():
    return cf.config


@app.route('/config-keys')
def keys():
    return json.dumps(list(cf.get_keys()))
