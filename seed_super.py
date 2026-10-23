import os
import secrets

from core import create_app
from core.extensions import db
from modules.user import User
from modules.user.role_service import ensure_default_roles


DEMO_USERS = [
    {"username": "maya.putri", "email": "maya.putri@example.test", "full_name": "Maya Putri"},
    {"username": "rafi.aditya", "email": "rafi.aditya@example.test", "full_name": "Rafi Aditya"},
    {"username": "nadia.safitri", "email": "nadia.safitri@example.test", "full_name": "Nadia Safitri"},
    {"username": "bima.prakoso", "email": "bima.prakoso@example.test", "full_name": "Bima Prakoso"},
]


def seed_initial_data():
    """Seed the administrator, default roles, and demo users into migrated tables."""
    username = os.getenv("SEED_ADMIN_USERNAME", "").strip()
    password = os.getenv("SEED_ADMIN_PASSWORD", "")
    if not username or not password:
        raise RuntimeError("Set SEED_ADMIN_USERNAME and SEED_ADMIN_PASSWORD before seeding.")

    ensure_default_roles()

    created = []
    if not User.query.filter_by(username=username).first():
        admin = User(username=username, full_name=username, is_active=True)
        admin.set_password(password)
        db.session.add(admin)
        created.append(username)

    for data in DEMO_USERS:
        if User.query.filter_by(username=data["username"]).first():
            continue
        demo_user = User(**data, is_active=True)
        # Demo accounts are for listing only; no reusable demo password is stored in source.
        demo_user.set_password(secrets.token_urlsafe(32))
        db.session.add(demo_user)
        created.append(data["username"])

    if not created:
        print("No users to create; the initial and demo users already exist.")
        return
    db.session.commit()
    print(f"Created {len(created)} user(s): {', '.join(created)}.")


if __name__ == "__main__":
    app = create_app()
    with app.app_context():
        seed_initial_data()
