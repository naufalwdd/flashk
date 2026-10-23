import os

from flask import Flask

from core.config import Config
from core.extensions import db, jwt, migrate
from core.routes import register_routes


def create_app(config_object=Config):
    """Create and configure the Flask application."""
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_object)
    os.makedirs(app.instance_path, exist_ok=True)

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    # Import feature models here as they are added so Flask-Migrate can discover them.
    from modules.auth.auth_model import RevokedToken  # noqa: F401
    from modules.user import Role, User  # noqa: F401

    register_routes(app)
    return app
