import os
from flask import Flask
from flask_login import LoginManager
from .config import Config
from .db import db, init_db

login_manager = LoginManager()

def create_app():
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config) # TODO: add values to .env

    # create instance path for app.db (to generate the database instance)
    os.makedirs(app.instance_path, exist_ok=True)

    # initial extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = "auth.login_form" # redirect to login page

    # import models after db init
    from .models import User, Profile

    @login_manager.user_loader
    def load_user(uid: str):
        return User.query.get((int(uid)))

    # import blueprints after app exists
    from .routes import bp as main_bp
    from .auth import bp as auth_bp
    from .profile import bp as profile_bp

    # register blueprints (api endpoints)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    print(app.url_map)

    with app.app_context():
        init_db()

    return app
