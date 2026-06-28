from functools import wraps

from flask import request, jsonify, g

import jwt

from config import Config


def require_auth(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        auth = request.headers.get(
            "Authorization"
        )

        if not auth:

            return jsonify({
                "message":
                "Token Missing"
            }), 401

        try:

            token = auth.split(" ")[1]

            decoded = jwt.decode(
                token,
                Config.SECRET_KEY,
                algorithms=["HS256"]
            )

            g.user = decoded

        except:

            return jsonify({
                "message":
                "Invalid Token"
            }), 401

        return func(*args, **kwargs)

    return wrapper