from flask import request, jsonify, g

from bson import ObjectId

from utils.db import posts_collection

from middlewares.auth_middleware import require_auth


@require_auth
def create_post():

    data = request.json

    posts_collection.insert_one({

        "user_email": g.user["email"],

        "caption": data.get("caption"),

        "description": data.get("description"),

        "required_skill": data.get("required_skill"),

        "budget": data.get("budget"),

        "deadline": data.get("deadline"),

        "image": data.get("image"),

        "likes": [],

        "comments": []
    })

    return jsonify({
        "message": "Post Created Successfully"
    })


@require_auth
def get_posts():

    posts = []

    for post in posts_collection.find():

        post["_id"] = str(post["_id"])

        posts.append(post)

    return jsonify({
        "posts": posts
    })


@require_auth
def like_post(post_id):

    user_email = g.user["email"]

    post = posts_collection.find_one({
        "_id": ObjectId(post_id)
    })

    if not post:

        return jsonify({
            "message": "Post Not Found"
        }), 404

    if user_email not in post["likes"]:

        posts_collection.update_one(
            {"_id": ObjectId(post_id)},
            {
                "$push": {
                    "likes": user_email
                }
            }
        )

    return jsonify({
        "message": "Post Liked"
    })


@require_auth
def comment_post(post_id):

    data = request.json

    comment = {

        "user": g.user["email"],

        "text": data["text"]
    }

    posts_collection.update_one(
        {
            "_id": ObjectId(post_id)
        },
        {
            "$push": {
                "comments": comment
            }
        }
    )

    return jsonify({
        "message": "Comment Added"
    })