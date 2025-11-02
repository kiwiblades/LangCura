from flask import Blueprint, render_template, jsonify, request
from flask_login import login_required, current_user
from . import bp
from ..db import db
from ..models import Profile

@bp.get("/")
@login_required
def page():
    # server renders the page, js fetches data to populate
    return render_template("meow.html")

@bp.get("/data")
@login_required
def get_profile():
    # retrieve the current user's profile
    profile = Profile.query.filter_by(uid=current_user.id).first()
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    
    return jsonify({
        "conditions": profile.conditions or "",
        "symptoms": profile.symptoms or "",
        "medications": profile.medications or "",
        "allergies": profile.allergies or "",
        "surgeries": profile.surgeries or "",
        "vaccines": profile.vaccines or "",
        "family_history": profile.family_history or "",
    })

@bp.put("/")
@login_required
def update_profile():
    # update the current user's profile (full replace)
    profile = Profile.query.filter_by(uid=current_user.id).first()
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    
    data = (request.get_json(silent=True) or {}) # get json if available, no error if none
    profile.conditions = data.get("conditions", profile.conditions)
    profile.symptoms = data.get("symptoms", profile.symptoms)
    profile.medications = data.get("medications", profile.medications)
    profile.allergies = data.get("allergies", profile.allergies)
    profile.surgeries = data.get("surgeries", profile.surgeries)
    profile.vaccines = data.get("vaccines", profile.vaccines)
    profile.family_history = data.get("family_history", profile.family_history)

    db.session.commit()

    # return the new state so frontend can immediately load the new data (without another get)
    return jsonify({
        "ok": True,
        "profile": {
            "conditions": profile.conditions or "",
            "symptoms": profile.symptoms or "",
            "medications": profile.medications or "",
            "allergies": profile.allergies or "",
            "surgeries": profile.surgeries or "",
            "vaccines": profile.vaccines or "",
            "family_history": profile.family_history or "",
        }
    }), 200