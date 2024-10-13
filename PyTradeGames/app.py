"""Creation and managing of the app, app settings and app factory."""

from flask import Flask
from .ext import configuration

import os


def create_app():
    template_dir = os.path.abspath('PyTradeGames/blueprints/webui/templates')
    static_dir = os.path.abspath('PyTradeGames/blueprints/webui/static')
    app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)
    configuration.init_app(app)

    return app
