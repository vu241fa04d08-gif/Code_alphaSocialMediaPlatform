from bcrypt import hashpw, gensalt, checkpw

def hash_password(password):

    return hashpw(
        password.encode(),
        gensalt()
    )


def verify_password(password, hashed_password):

    return checkpw(
        password.encode(),
        hashed_password
    )