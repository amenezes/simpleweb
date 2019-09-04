import os
import logging

from config.cf import CF
from config.spring import ConfigClient

from flask import Flask, escape, request, jsonify


logger = logging.getLogger('gunicorn.error')
logger.setLevel(logging.INFO)

#logging.error(os.environ)

cf = CF()
cf.get_config()
#cf = ConfigClient(
#    app_name='configserver',
#    branch='ft-sdintegracoes-591'
#)
#cf.get_config()


app = Flask(__name__)


def show_config():
    return cf.config

@app.route('/')
def hello():
    name = request.args.get("name", "World")
    return f'Hello, {escape(name)}!'


@app.route('/config')
def config():
    return show_config()
