from modules.user import User


def list_users():
    return [user.to_dict() for user in User.query.order_by(User.id.asc()).all()]
