import os, json, time, hashlib
from typing import Tuple, Any, Dict
from openai import OpenAI

FIELDS = [
    "symptoms", "medications", "conditions",
    "allergies", "surgeries", "vaccines", "family_history"
]

# in memory cache
CACHE: dict[tuple[int, str, str], tuple[float, dict]] = {}
CACHE_SECS = 60 * 60 # 1 hour



def get_client():
    key = os.getenv("OPENROUTER_KEY")
    base = os.getenv("OPENROUTER_BASE", "https://openrouter.ai/api/v1")
    if not key:
        raise RuntimeError("Missing OPENROUTER_KEY in env")
    return OpenAI(api_key=key, base_url=base)

def translate_profile(profile: Dict[str, Any],
                      target_lang: str="es",
                      source_lang: str="auto") -> Tuple[bool, Dict[str, str] | str]:
    
    client = get_client()
    src = {k: (profile.get(k) or "") for k in FIELDS}

    prompt = (
        "You are a medical translator whose job is to translate a patient's profile medical data to another language,"
        "for the use of healthcare providers. Translate faithfully and thoroughly."
        "Translate each field of the given PROFILE_JSON into TARGET_LANG." 
        "Do not add or omit meaning. If unsure of a drug name or medical term, keep it as written."
        "Do not offer any medical advice or provide any other information besides the exact translation of the patient's text." 
        "Return ONLY a JSON object with the SAME KEYS you received "
        "(symptoms, medications, conditions, allergies, surgeries, vaccines, family_history)."
    )

    try:
        resp = client.chat.completions.create(
            model=os.getenv("OPENROUTER_MODEL", "google/gemini-2.0-flash-001"),
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content":
                    f"TARGET_LANG={target_lang}\nSOURCE_LANG={source_lang}\n"
                    f"PROFILE_JSON:\n{json.dumps(src, ensure_ascii=False)}"},
            ],
            temperature=0.0,
            response_format={"type": "json_object"},
        )
        raw = resp.choices[0].message.content or "{}"
        data = json.loads(raw)
        # ensure every expected key exists and is a string
        out = {}
        for k in FIELDS:
            v = data.get(k, "")
            out[k] = "" if v is None else str(v)
        return True, out
    except Exception as json_mode_err:
        json_error = str(json_mode_err)

# def translate_cache(
#         uid: int,
#         profile: Dict[str, Any],
#         target_lang: str = "es",
#         source_lang: str = "auto"
# ) -> Tuple[bool, Dict[str,str] | str]:
#     # in-memory cache for profile translations
    

