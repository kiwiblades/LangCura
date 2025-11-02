import os
from openai import OpenAI

def get_client():
    key = os.getenv("OPENROUTER_KEY")
    base = os.getenv("OPENROUTER_BASE", "https://openrouter.ai/api/v1")
    if not key:
        raise RuntimeError("Missing OPENROUTER_KEY in env")
    return OpenAI(api_key=key, base_url=base)

def translate_text(text:str, source_lang:str, target_lang:str) -> str | None:
    # if no text, return empty, don't bother translator
    if not text:
        return ""
    
    prompt = (
        "You are a medical translator whose job is to translate a patient's profile medical data to another language,"
        "for the use of healthcare providers. Translate faithfully and thoroughly."
        "Do not add or omit meaning. If unsure of a drug name or medical term, keep it as written."
        "Do not offer any medical advice or provide any other information besides the exact translation of the patient's text." 
        "Output only the translation text."
    )
    user = f"Source language: {source_lang}\nTarget language: {target_lang}\n\nText:\n{text}"

    client = get_client()
    try:
        response = client.chat.completions.create(
            model=os.getenv("OPENROUTER_MODEL","google/gemini-2.0-flash-001"),
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": user},
            ],
            temperature=0.0 # disable response variety, must be objective
        )
        return (response.choices[0].message.content or "").strip()
    except Exception as e:
        # log e for debugging if needed
        return None
