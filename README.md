# LangCura

LangCura is a medical translation assistant designed to help Spanish-speaking patients communicate health information during medical visits or emergencies.

It focuses on translating structured medical data, such as allergies, medications, and medical conditions, into English to reduce communication barriers between patients and healthcare providers.

## Problem

In emergency or clinical settings, language barriers can delay care or result in incomplete medical information. General translation tools may not capture structured medical context accurately or quickly.

LangCura was built to provide fast, focused translation of essential medical information in a structured format.

## Context

LangCura was built during Hack OKState '25, a 24-hour hackathon focused on local community impact.

In our area, Spanish-speaking patients are often underserved in healthcare settings, particularly in urgent or high-stress situations. We wanted to explore how structured AI-assisted translation could help reduce communication barriers in those moments.

The time constraint required prioritizing core functionality and clean architectural separation over polish and production deployment.

## Features
- Structured input fields for:
    - Symptoms
    - Medications
    - Conditions
    - Allergies
    - Surgeries
    - Vaccines
    - Family History
- AI-powered medical translation
- Basic login/logout backend functionality
- Lightweight multilingual HTML/CSS interface for rapid input

## Tech Stack
- **Backend:** Python, Flask
- **AI Integration:** OpenRouter (LLM-based translation)
- **Frontend:** HTML, CSS, minimal JavaScript
- **Environment:** Python virtual environment

## Architecture Overview

LangCura uses a Flask backend to handle structured medical input, send translation requests to the OpenRouter API, and return translated results to the frontend.

The system separates:
- UI structure and form handling
- Backend request processing
- AI translation logic

This separation allowed rapid iteration during the hackathon while maintaining clear logical boundaries.

## My Role

I implemented the backend logic, AI integration, and request handling.
My teammate contributed to interface design and helped refine translation phrasing, leveraging native Spanish fluency.

## Setup

```bash
python -m venv venv
source venv/bin/activate # or venv\Scripts\activate on Windows
python -m pip install -r requirements.txt
python run.py
```

## Future Improvements
- Context-aware medical terminology handling
- Deployment with secure environment configuration
- Expanded language support
- Provider-facing formatting improvements