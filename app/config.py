import os
from pathlib import Path

class Config:
    # in prodction, values are replaced
    SECRET_KEY = os.getenv("SECRET_KEY", "dev_secret")
    INSTANCE_PATH = os.getenv("INSTANCE_PATH", Path("instance"))
    DB_PATH = os.getenv("DB_PATH", "dev.db")
    SQLALCHEMY_DATABASE_URI = os.getenv(
        "DATABASE_URL",
        f"sqlite:///{Path(INSTANCE_PATH).absolute()/DB_PATH}"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False