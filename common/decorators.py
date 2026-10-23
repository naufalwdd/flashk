from functools import wraps
import logging

from flask import current_app, redirect, request, session, url_for
from flask_jwt_extended import verify_jwt_in_request

from common.response import error

logger = logging.getLogger(__name__)


def log_errors(function):
    """Log an unexpected endpoint error, then let Flask handle the exception."""
    @wraps(function)
    def wrapped(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except Exception:
            logger.exception("Unhandled error in %s", function.__qualname__)
            raise

    return wrapped


def protected(function):
    """Protect an endpoint using application secret key, JWT, or browser-session flow."""
    @wraps(function)
    def wrapped(*args, **kwargs):
        supplied_secret = request.headers.get("X-Secret-Key")
        configured_secret = current_app.config.get("SECRET_KEY")
        if supplied_secret and supplied_secret == configured_secret:
            return function(*args, **kwargs)

        try:
            verify_jwt_in_request()
        except Exception:
            # Missing or invalid tokens fall through to the session check
            pass
        else:
            return function(*args, **kwargs)

        if session.get("username"):
            return function(*args, **kwargs)

        if "text/html" in request.headers.get("Accept", ""):
            return redirect(url_for("web.login_page"))
        return error("Unauthorized. Harap login terlebih dahulu.", 401)

    return wrapped
