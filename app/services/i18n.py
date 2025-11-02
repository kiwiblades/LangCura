STRINGS = {
    "en": {
        # General
        "language": "Language",
        "back": "Back",
        "print": "Print",

        # Nav
        "nav_home": "Home",
        "nav_profile": "Profile",
        "nav_translate": "Translate",
        "nav_login": "Login",
        "nav_register": "Register",
        "nav_signout": "Signout",

        # Home
        "home_title": "Home",
        "home_welcome": "Welcome! Please register or sign in.",
        "home_signed_in_as": "You're signed in as",

        # Auth
        "login_title": "Login",
        "login_email": "Email",
        "login_password": "Password",
        "login_submit": "Login",
        "register_title": "Register",
        "register_submit": "Create account",
        "email_placeholder": "",

        # Profile page
        "profile_title": "Your Medical Profile",
        "greeting": "Hello! Please take a moment to fill out the following:",
        "edit": "Edit",
        "submit": "Save",
        "cancel": "Cancel",
        "provider_card": "Provider Card",
        "provider_card_lang": "Provider Card ({lang})",

        # Read-only labels
        "symptoms": "Symptoms",
        "medications": "Medications",
        "conditions": "Conditions",
        "allergies": "Allergies",
        "surgeries": "Surgeries",
        "vaccines": "Vaccinations",
        "family_history": "Family History",

        # Edit labels
        "symptoms_edit": "Describe your symptoms",
        "medications_edit": "List any medications",
        "conditions_edit": "Pre-existing medical conditions",
        "allergies_edit": "Allergies (medications/foods)",
        "surgeries_edit": "Past surgeries / procedures",
        "vaccines_edit": "Vaccination Record",
        "family_edit": "Family medical history",

        # Profile placeholders
        "ph_symptoms": "List symptoms, one per line…",
        "ph_meds": "Drug name, dose, frequency…",
        "ph_conditions": "Diabetes, asthma, etc.",
        "ph_allergies": "Penicillin, peanuts, etc.",
        "ph_surgeries": "Appendectomy (2019), …",
        "ph_vaccines": "COVID-19 (2023 booster), Tdap (2022), …",
        "ph_family": "Parent: hypertension; sibling: asthma; …",

        # Card
        "card_title": "Patient Summary",
        "card_language": "Language",
        "card_user": "User",
        "switch_to_en": "Switch to English",
        "switch_to_es": "Cambiar a Español",
        "none": "(none)",

        # Front page tiles
        "card_profile_title": "Profile",
        "card_profile_body": "Keep symptoms, meds, and history up to date. Edit in your language—we’ll handle the rest.",
        "card_profile_link": "Go to Profile",

        "card_card_title": "Provider Card",
        "card_card_body": "Generate a clean, printable summary for clinicians in {LANG} (switch languages on the top bar).",
        "card_card_link": "Open Card",

        "card_lang_title": "Language",
        "card_lang_body": "Prefer English or Español? Use the selector above—your choice is saved for next time.",
        "card_lang_link": "Change language",
        
    },
    "es": {
        # General
        "language": "Idioma",
        "back": "Volver",
        "print": "Imprimir",

        # Nav
        "nav_home": "Inicio",
        "nav_profile": "Perfil",
        "nav_translate": "Traducir",
        "nav_login": "Ingresar",
        "nav_register": "Registrarse",
        "nav_signout": "Salir",

        # Home
        "home_title": "Inicio",
        "home_welcome": "¡Bienvenido/a! Regístrese o inicie sesión.",
        "home_signed_in_as": "Has iniciado sesión como",

        # Auth
        "login_title": "Ingresar",
        "login_email": "Correo electrónico",
        "login_password": "Contraseña",
        "login_submit": "Ingresar",
        "register_title": "Registrarse",
        "register_submit": "Crear cuenta",

        # Profile page
        "profile_title": "Tu perfil médico",
        "greeting": "¡Hola! Por favor, dedique un momento a completar lo siguiente:",
        "edit": "Editar",
        "submit": "Guardar",
        "cancel": "Cancelar",
        "provider_card": "Tarjeta para el proveedor",
        "provider_card_lang": "Tarjeta para el proveedor ({lang})",

        # Read-only labels
        "symptoms": "Síntomas",
        "medications": "Medicamentos",
        "conditions": "Condiciones",
        "allergies": "Alergias",
        "surgeries": "Cirugías",
        "vaccines": "Vacunas",
        "family_history": "Antecedentes familiares",

        # Edit labels
        "symptoms_edit": "Describa sus síntomas",
        "medications_edit": "Enumere los medicamentos que toma",
        "conditions_edit": "Afecciones médicas preexistentes",
        "allergies_edit": "Alergias (medicamentos/alimentos)",
        "surgeries_edit": "Cirugías / procedimientos previos",
        "vaccines_edit": "Vacunas",
        "family_edit": "Antecedentes médicos familiares",

        # Placeholders
        "ph_symptoms": "Enumere los síntomas, uno por línea…",
        "ph_meds": "Nombre del medicamento, dosis, frecuencia…",
        "ph_conditions": "Diabetes, asma, etc.",
        "ph_allergies": "Penicilina, cacahuates, etc.",
        "ph_surgeries": "Apendicectomía (2019), …",
        "ph_vaccines": "COVID-19 (refuerzo 2023), Tdpa (2022), …",
        "ph_family": "Progenitor: hipertensión; hermano/a: asma; …",

        # Card
        "card_title": "Resumen del paciente",
        "card_language": "Idioma",
        "card_user": "Usuario",
        "switch_to_en": "Switch to English",
        "switch_to_es": "Cambiar a Español",
        "none": "(ninguno)",

        # Front page tiles
        "card_profile_title": "Perfil",
        "card_profile_body": "Mantén actualizados tus síntomas, medicamentos e historial. Edita en tu idioma; nosotros nos encargamos del resto.",
        "card_profile_link": "Ir al Perfil",

        "card_card_title": "Tarjeta para el proveedor",
        "card_card_body": "Genera un resumen limpio e imprimible para profesionales en {LANG} (puedes cambiar el idioma en la barra superior).",
        "card_card_link": "Abrir Tarjeta",

        "card_lang_title": "Idioma",
        "card_lang_body": "¿Prefieres inglés o español? Usa el selector de arriba; tu elección se guardará para la próxima vez.",
        "card_lang_link": "Cambiar idioma",
    },
}

def t(key, lang):
    return STRINGS.get(lang, STRINGS["en"]).get(key, STRINGS["en"].get(key, key))