from flask import Blueprint, jsonify

from common.decorators import protected
from modules.user.role_service import list_roles

role_blueprint = Blueprint("roles", __name__, url_prefix="/api/roles")


@role_blueprint.get("")
@protected
def get_roles():
    return jsonify({"success": True, "data": list_roles()})
