import os
from flask import Flask
from .config import Config
from .extensions import db, login_manager

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # create instance path for app.db
    os.makedirs(app.instance_path, exist_ok=True)

    # initial extensions
    db.init_app(app)
    login_manager.init_app(app)

    # register blueprints (api endpoints)
    # TODO: create api for each new function
    # from .routes.pages import bp as pages_bp

    with app.app_context():
        from . import models
        db.create_all()

    return app
