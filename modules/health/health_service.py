from datetime import datetime, timezone


def get_health_status():
    return {
        "status": "healthy",
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
