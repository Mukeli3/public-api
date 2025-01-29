#!/usr/bin/python3
from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)
    CORS(app)

    from app.route import main
    app.register_blueprint(main)

    return app
