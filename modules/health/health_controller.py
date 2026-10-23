from flask import Blueprint

from common.response import success
from modules.health.health_service import get_health_status

health_blueprint = Blueprint("health", __name__, url_prefix="/api")


@health_blueprint.get("/health")
def health():
    return success(data=get_health_status(), message="Service is healthy")
