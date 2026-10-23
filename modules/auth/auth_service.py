from flask_jwt_extended import create_access_token

from core.extensions import db, jwt
from modules.auth.auth_model import RevokedToken
from modules.user import User


@jwt.token_in_blocklist_loader
def is_token_revoked(jwt_header, jwt_payload):
    return RevokedToken.query.filter_by(jti=jwt_payload["jti"]).first() is not None


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user is None or not user.is_active or not user.check_password(password):
        return None

    return {
        "access_token": create_access_token(identity=str(user.id)),
        "user": user.to_dict(),
    }


def revoke_token(jti):
    if not RevokedToken.query.filter_by(jti=jti).first():
        db.session.add(RevokedToken(jti=jti))
        db.session.commit()
