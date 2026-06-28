from flask import jsonify

from utils.db import (
    profiles_collection,
    posts_collection,
    requests_collection
)

from middlewares.auth_middleware import require_auth


@require_auth
def get_stats():

    return jsonify({

        "creators":
        profiles_collection.count_documents({}),

        "posts":
        posts_collection.count_documents({}),

        "requests":
        requests_collection.count_documents({})
    })