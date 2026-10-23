from flask import Blueprint, jsonify, request, session
from flask_jwt_extended import get_jwt, verify_jwt_in_request
from flask_jwt_extended.exceptions import JWTExtendedException

from common.decorators import protected
from common.response import error
from modules.auth.auth_service import authenticate, revoke_token

auth_blueprint = Blueprint("auth", __name__, url_prefix="/api/auth")


@auth_blueprint.post("/login")
def login():
    payload = request.get_json(silent=True) or {}
    username = payload.get("username", "")
    password = payload.get("password", "")
    if not isinstance(username, str) or not isinstance(password, str):
        return error("Username dan password wajib diisi.", 422)

    username = username.strip()
    if not username or not password:
        return error("Username dan password wajib diisi.", 422)

    result = authenticate(username, password)
    if result is None:
        return error("Username atau password salah.", 401)

    # The browser UI uses the session; API clients can use the returned Bearer token.
    session["username"] = result["user"]["username"]
    session["user_id"] = result["user"]["id"]
    return jsonify({"success": True, "message": "Login berhasil.", "data": result})


@auth_blueprint.post("/logout")
@protected
def logout():
    try:
        verify_jwt_in_request(optional=True)
    except JWTExtendedException:
        # A valid browser session is enough to end the web login, even if an old
        # bearer token was also sent with the request.
        pass
    else:
        token_data = get_jwt()
        if token_data:
            revoke_token(token_data["jti"])

    session.clear()
    return jsonify({"success": True, "message": "Logout berhasil."})
