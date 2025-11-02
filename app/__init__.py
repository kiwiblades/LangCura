import os
from flask import Flask, g, request, redirect, url_for, session
from flask_login import LoginManager, current_user, login_required
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
    from .translate import bp as translate_bp

    # register blueprints (api endpoints)
    app.register_blueprint(main_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(translate_bp)

    with app.app_context():
        init_db()

    # check the user's language before rendering content
    @app.before_request
    def choose_lang():
        sess_lang = (session.get("lang") or "").lower()
        if sess_lang in ("en", "es"):
            g.lang = sess_lang
            return

        arg_lang = (request.args.get("lang") or "").lower()
        if arg_lang in ("en", "es"):
            session["lang"] = arg_lang
            g.lang = arg_lang
            return

        if current_user.is_authenticated:
            g.lang = (getattr(current_user, "preferred_language", "en") or "en").lower()
            return
        
        # default to english
        g.lang = "en"

    # import language services
    from .services.i18n import t as _t
    @app.context_processor
    def inject_i18n():
        return {
            "t": _t,
            "LANG": getattr(g, "lang", "en"),
    }


    @app.post("/lang")
    def set_lang():
        lang = (request.form.get("lang") or "en").lower()
        if lang not in ("en","es"):
            lang = "en"
        session["lang"] = lang # change takes place immediately in session
        current_user.preferred_language = lang # persist to db
        db.session.commit()
        return redirect(request.referrer or url_for("main.index"))

    return app
