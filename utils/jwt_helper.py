import jwt
import time

from config import Config


def generate_token(email):

    token = jwt.encode(
        {
            "email": email,
            "exp": int(time.time()) + 86400
        },
        Config.SECRET_KEY,
        algorithm="HS256"
    )

    return token