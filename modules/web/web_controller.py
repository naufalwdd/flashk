from flask import Blueprint, render_template

from common.decorators import protected

web_blueprint = Blueprint(
    "web",
    __name__,
    template_folder="templates",
    static_folder="static",
    static_url_path="/web-static",
)


@web_blueprint.get("/")
@web_blueprint.get("/login")
def login_page():
    return render_template("login.jinja")


@web_blueprint.get("/app")
@protected
def dashboard_page():
    return render_template("pages/dashboard.jinja", active_page="dashboard", page_title="Dashboard")


@web_blueprint.get("/app/users")
@protected
def users_page():
    return render_template("pages/users.jinja", active_page="users", page_title="Users")


@web_blueprint.get("/app/roles")
@protected
def roles_page():
    return render_template("pages/roles.jinja", active_page="roles", page_title="Roles")


@web_blueprint.get("/app/reports")
@protected
def reports_page():
    return render_template("pages/reports.jinja", active_page="reports", page_title="Reports")


@web_blueprint.get("/app/settings")
@protected
def settings_page():
    return render_template("pages/settings.jinja", active_page="settings", page_title="Settings")
