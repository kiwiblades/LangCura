from flask import request, jsonify, render_template, g
from flask_login import login_required, current_user
from . import bp
from ..models import Profile
from ..services.ai_client import translate_profile # TODO: create fcn

SUPPORTED = {"en", "es"}

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

@bp.get("/card")
@login_required
def provider_card():
    target = (request.args.get("lang") or getattr(g, "lang", "es")).lower()
    if target not in SUPPORTED:
        target = "es"

    prof = Profile.query.filter_by(uid=current_user.id).first()
    # if not prof:
        # return render_template("translate/error.html", msg="Profile not found"), 404

    src = {
        "symptoms": prof.symptoms or "",
        "medications": prof.medications or "",
        "conditions": prof.conditions or "",
        "allergies": prof.allergies or "",
        "surgeries": prof.surgeries or "",
        "vaccines": prof.vaccines or "",
        "family_history": prof.family_history or "",
    }

    ok, translated = translate_profile(src, target)
    # if not ok

    other = "es" if target == "en" else "en"

    # translated is a dict with the same keys
    return render_template("card.html",
                           lang=target, other_lang=other, p=translated, user=current_user)
