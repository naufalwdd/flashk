import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "local-development-only")
    DEBUG = os.getenv("FLASK_DEBUG", "false").lower() in {"1", "true", "yes"}
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///flashk.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", SECRET_KEY)
    JWT_TOKEN_LOCATION = ["headers"]
    JWT_ACCESS_TOKEN_EXPIRES = 60 * 60
