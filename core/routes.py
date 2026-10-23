from modules.auth.auth_controller import auth_blueprint
from modules.dashboard.dashboard_controller import dashboard_blueprint
from modules.health.health_controller import health_blueprint
from modules.user.role_controller import role_blueprint
from modules.user.user_controller import user_blueprint
from modules.web.web_controller import web_blueprint


def register_routes(app):
    """Register all feature blueprints in one place."""
    app.register_blueprint(web_blueprint)
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(user_blueprint)
    app.register_blueprint(role_blueprint)
    app.register_blueprint(dashboard_blueprint)
    app.register_blueprint(health_blueprint)
