from flask import jsonify


def success(data=None, message="OK", status=200):
    return jsonify({"success": True, "message": message, "data": data}), status


def error(message="An error occurred", status=400, details=None):
    body = {"success": False, "message": message}
    if details is not None:
        body["details"] = details
    return jsonify(body), status
