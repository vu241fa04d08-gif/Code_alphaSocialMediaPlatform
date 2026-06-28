from flask import request, jsonify, g

from bson import ObjectId

from utils.db import requests_collection

from middlewares.auth_middleware import require_auth


@require_auth
def send_request():

    data = request.json

    requests_collection.insert_one({

        "from_user": g.user["email"],

        "to_user": data["to_user"],

        "message": data["message"],

        "status": "Pending",

        "seen": False
    })

    return jsonify({
        "message": "Request Sent"
    })


@require_auth
def get_requests():

    result = []

    for req in requests_collection.find({

        "$or": [

            {"from_user": g.user["email"]},

            {"to_user": g.user["email"]}
        ]
    }):

        req["_id"] = str(req["_id"])

        result.append(req)

    return jsonify({
        "requests": result
    })


@require_auth
def accept_request(request_id):

    requests_collection.update_one(
        {
            "_id": ObjectId(request_id)
        },
        {
            "$set": {
                "status": "Accepted"
            }
        }
    )

    return jsonify({
        "message": "Request Accepted"
    })


@require_auth
def reject_request(request_id):

    requests_collection.update_one(
        {
            "_id": ObjectId(request_id)
        },
        {
            "$set": {
                "status": "Rejected"
            }
        }
    )

    return jsonify({
        "message": "Request Rejected"
    })