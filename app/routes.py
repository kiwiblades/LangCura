from flask import Blueprint, render_template, url_for, redirect, session, request
from flask_login import current_user, login_required
from .db import db

bp = Blueprint("main", __name__)

@bp.get("/")
def index():
    return render_template("index.html")

@bp.get("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")