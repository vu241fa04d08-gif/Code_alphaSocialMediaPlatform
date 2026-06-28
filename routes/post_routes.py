from flask import Blueprint
from controllers.post_controller import (
    create_post,
    get_posts,
    like_post,
    comment_post
)

post_bp = Blueprint("post_bp", __name__)

post_bp.add_url_rule("/posts", view_func=create_post, methods=["POST"])
post_bp.add_url_rule("/posts", view_func=get_posts, methods=["GET"])

post_bp.add_url_rule("/posts/<post_id>/like", view_func=like_post, methods=["POST"])
post_bp.add_url_rule("/posts/<post_id>/comment", view_func=comment_post, methods=["POST"])