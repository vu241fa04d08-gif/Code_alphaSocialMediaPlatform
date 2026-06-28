from flask import request, jsonify, g

from utils.db import profiles_collection

from middlewares.auth_middleware import require_auth


@require_auth
def create_profile():

    data = request.json

    profiles_collection.insert_one({

        "email": g.user["email"],

        "name": data.get("name"),

        "profile_image": data.get("profile_image"),

        "category": data.get("category"),

        "city": data.get("city"),

        "skills": data.get("skills"),

        "followers": data.get("followers"),

        "bio": data.get("bio"),

        "portfolio": data.get("portfolio")
    })

    return jsonify({
        "message": "Profile Created Successfully"
    })


@require_auth
def get_profiles():

    profiles = []

    for profile in profiles_collection.find():

        profile["_id"] = str(profile["_id"])

        profiles.append(profile)

    return jsonify({
        "profiles": profiles
    })