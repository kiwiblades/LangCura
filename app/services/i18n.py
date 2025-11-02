STRINGS = {
    "en": {
        "site_title": "Lingcura",
        "greeting": "Hello! Please take a moment to fill out the following:",
        "edit": "Edit",
        "submit": "Submit",
        "cancel": "Cancel",
        "symptoms": "Symptoms",
        "symptoms_edit": "Describe your symptoms",
        "medications": "Medications",
        "medications_edit": "List any medications",
        "conditions": "Conditions",
        "conditions_edit": "Pre-existing medical conditions",
        "allergies": "Allergies",
        #TODO: allergies_edit
        "surgeries": "Surgeries",
        #TODO: surgeries_edit
        "vaccines": "Vaccinations",
        #TODO: vaccines_edit
        "family_history": "Family Medical History",
        #TODO: family_edit
    },
    "es": {
        "site_title": "Lingcura",
        "greeting": "¡Hola! Por favor, dedique un momento a completar lo siguiente:",
        "edit": "Editar",
        "submit": "Guardar",
        "cancel": "Cancelar",
        "symptoms": "Síntomas",
        "symptoms_edit": "Describa sus síntomas",
        "medications": "Medicamentos",
        "medications_edit": "Enumere los medicamentos que toma",
        "conditions": "Condiciones",
        "conditions_edit": "Afecciones médicas preexistentes",
        "allergies": "Alergias",
        #TODO: allergies_edit
        "surgeries": "Cirugías",
        #TODO: surgeries_edit
        "vaccines": "Vacunas",
        #TODO: vaccines_edit
        "family_history": "Antecedentes familiares",
        #TODO: family_edit
    },
}

def t(key, lang):
    return STRINGS.get(lang, STRINGS["en"]).get(key, key)