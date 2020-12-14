from flask import Flask


def create_app():
    allegrosz = Flask(__name__)

    from .vievs import bp_main

    allegrosz.register_blueprint(bp_main)

    return allegrosz
