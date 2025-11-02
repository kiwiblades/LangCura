from flask import request, jsonify, render_template
from flask_login import login_required, current_user
from . import bp
from ..models import Profile
from ..services.ai_client import translate_profile # TODO: create fcn

@bp.post("/profile")
@login_required
def translate_pf():
    target = (request.json or {}).get("lang", "es").lower()

    prof = Profile.query.filter_by(uid=current_user.id).first()
    if not prof:
        return jsonify({"error": "[Translate] Profile not found"}), 404

    src = {
        "symptoms": prof.symptoms, "medications": prof.medications, "conditions": prof.conditions,
        "allergies": prof.allergies, "surgeries": prof.surgeries, "vaccines": prof.vaccines,
        "family_history": prof.family_history,
    }
    translated = translate_profile(src, target)
    return jsonify({"ok": True, "lang": target, "translated": translated})
