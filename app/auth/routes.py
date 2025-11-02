from flask import flash, render_template, g, redirect, url_for, request
from flask_login import login_user, logout_user, login_required, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from . import bp
from ..db import db
from ..models import User, Profile

@bp.get("/register")
def register_form():
    return render_template("register.html")

@bp.post("/register")
def register_submit():
    # retrieve info from signup forms
    email = (request.form.get("email") or "").strip().lower()
    password = request.form.get("password") or ""
    if not email or not password:
        flash("Email and password required", "error")
        return redirect(url_for("auth.register_form"))
    if User.query.filter_by(email=email).first():
        flash("Email already registered", "error")
        return redirect(url_for("auth.register_form"))
    
    # create the user
    user = User(email=email, password_hash=generate_password_hash(password))
    db.session.add(user)
    db.session.flush() # flush first to create the profile

    # create a blank profile for the user
    profile = Profile(uid=user.id)
    db.session.add(profile)
    db.session.commit() # commit both user and profile

    # sign up successful, login and greet user
    # eventually, add email verification first
    login_user(user)
    flash("Welcome!", "success")
    return redirect(url_for("main.index"))

@bp.get("/login")
def login_form():
    return render_template("login.html")

@bp.post("/login")
def login_submit():
    email = (request.form.get("email") or "").strip().lower()
    password = request.form.get("password") or ""
    user = User.query.filter_by(email=email).first()
    if not user or not check_password_hash(user.password_hash, password):
        flash("Invalid credentials", "error")
        return redirect(url_for("auth.login_form"))
    login_user(user)
    flash("Signed in", "success")
    return redirect(url_for("main.index"))

@bp.route("/logout", methods=["GET","POST"])
@login_required
def logout():
    logout_user()
    flash("Signed out", "success")
    return redirect(url_for("main.index"))