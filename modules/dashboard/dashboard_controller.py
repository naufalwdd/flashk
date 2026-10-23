from flask import Blueprint, jsonify

from common.decorators import protected
from modules.dashboard.dashboard_service import (
    get_demo_report,
    get_demo_settings,
    get_demo_users,
    get_overview,
)

dashboard_blueprint = Blueprint("dashboard", __name__, url_prefix="/api")


@dashboard_blueprint.get("/dashboard/overview")
@protected
def overview():
    return jsonify({"success": True, "data": get_overview()})


@dashboard_blueprint.get("/demo/users")
@protected
def demo_users():
    return jsonify({"success": True, "data": get_demo_users()})


@dashboard_blueprint.get("/demo/reports")
@protected
def demo_reports():
    return jsonify({"success": True, "data": get_demo_report()})


@dashboard_blueprint.get("/demo/settings")
@protected
def demo_settings():
    return jsonify({"success": True, "data": get_demo_settings()})
