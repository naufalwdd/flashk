from flask import Blueprint, jsonify

from common.decorators import protected
from modules.user.user_service import list_users

user_blueprint = Blueprint("users", __name__, url_prefix="/api/users")


@user_blueprint.get("")
@protected
def get_users():
    return jsonify({"success": True, "data": list_users()})
