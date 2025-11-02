from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

def init_db():
    # ensure models are imported
    from .models import User, Profile
    db.create_all()