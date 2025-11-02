from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from ..models import Profile, db

bp = Blueprint("profile", __name__)

@bp.get("/")
@login_required
def get_profile():
    # retrieve the current user's profile
    profile = Profile.query.filter_by(uid=current_user.id).first()
    if not profile:
        return jsonify({"error": "Profile not found"}), 404
    
    return jsonify({
        "conditions": profile.conditions,
        "symptoms": profile.symptoms,
        "medications": profile.medications,
        "allergies": profile.allergies,
        "surgeries": profile.surgeries,
        "vaccines": profile.vaccines,
        "family_history": profile.family_history,
    })

@bp.put("/")
@login_required
def update_profile():
    # update the current user's profile (full replace)
    profile = Profile.query.filter_by(uid=current_user.id).first()
    if not profile:
        return jsonify({"error", "Profile not found"}), 404
    
    data = request.json
    profile.conditions = data.get("conditions", profile.conditions)
    profile.symptoms = data.get("symptoms", profile.symptoms)
    profile.medications = data.get("medications", profile.medications)
    profile.allergies = data.get("allergies", profile.alleriges)
    profile.surgeries = data.get("surgeries", profile.surgeries)
    profile.vaccines = data.get("vaccines", profile.vaccines)
    profile.family_history = data.get("family_history", profile.family_history)

    db.session.commit()
    return jsonify({"message": "Profile updated successfully"})