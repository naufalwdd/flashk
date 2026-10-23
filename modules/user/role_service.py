from core.extensions import db
from modules.user import Role


DEFAULT_ROLES = [
    {
        "name": "Admin",
        "slug": "admin",
        "description": "Akses penuh untuk mengelola workspace dan anggotanya.",
        "permissions": ["workspace:manage", "users:manage", "roles:manage", "reports:view"],
        "is_system": True,
    },
    {
        "name": "Editor",
        "slug": "editor",
        "description": "Mengelola konten workspace dan melihat laporan.",
        "permissions": ["content:manage", "reports:view"],
        "is_system": True,
    },
    {
        "name": "Member",
        "slug": "member",
        "description": "Berkolaborasi pada pekerjaan workspace.",
        "permissions": ["content:view", "content:edit"],
        "is_system": True,
    },
    {
        "name": "Viewer",
        "slug": "viewer",
        "description": "Melihat konten tanpa mengubah data.",
        "permissions": ["content:view", "reports:view"],
        "is_system": True,
    },
]


def ensure_default_roles():
    """Insert the demo roles that are missing, without overwriting custom edits."""
    for data in DEFAULT_ROLES:
        if not Role.query.filter_by(slug=data["slug"]).first():
            db.session.add(Role(**data))
    db.session.commit()


def list_roles():
    return [role.to_dict() for role in Role.query.order_by(Role.id.asc()).all()]
