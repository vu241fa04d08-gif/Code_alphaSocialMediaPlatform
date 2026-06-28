from flask import request, jsonify

def signup():
    data = request.json

    print("SIGNUP DATA:", data)

    return jsonify({
        "message": "Signup successful"
    }), 200


def login():
    data = request.json

    print("LOGIN DATA:", data)

    return jsonify({
        "message": "Login successful",
        "token": "demo-token"
    }), 200