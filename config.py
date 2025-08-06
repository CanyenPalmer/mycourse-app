# config.py

import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "default-secret-if-not-set")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL", "sqlite:///site.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    FLASK_ENV = os.environ.get("FLASK_ENV", "production")
# Placeholder for config.py
