from .db import db
from datetime import datetime, timezone
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import Integer, String, DateTime, ForeignKey
from flask_login import UserMixin

# user authentication data
class User(db.Model, UserMixin):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True) # sqlalchemy automatically autoincrements keys
    email = db.Column(db.String(255), unique=True, nullable=False, index=True)
    password_hash = db.Column(db.String(255), nullable=False)

    # logging data
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<User {self.id} {self.email}>"
    


# user medical information, nothing is required. user updates the info to translate to medical providers
class Profile(db.Model):
    __tablename__ = "profile"

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    user = relationship("User", backref="profile")
    
    # medical info
    symptoms = db.Column(db.Text)
    medications = db.Column(db.Text)
    conditions = db.Column(db.Text)
    allergies = db.Column(db.Text)
    surgeries = db.Column(db.Text)
    vaccines = db.Column(db.Text)
    family_history = db.Column(db.Text)

    # TODO: add all medical information fields

    # logging data
    created_at = db.Column(
        db.DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    def __repr__(self):
        return f"<Profile {self.id} for User {self.uid}>"