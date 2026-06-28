from flask import Blueprint

from controllers.request_controller import (
    send_request,
    get_requests,
    accept_request,
    reject_request
)

request_bp = Blueprint(
    "request_bp",
    __name__
)

request_bp.route(
    "/send-request",
    methods=["POST"]
)(send_request)

request_bp.route(
    "/requests",
    methods=["GET"]
)(get_requests)

request_bp.route(
    "/accept-request/<request_id>",
    methods=["PUT"]
)(accept_request)

request_bp.route(
    "/reject-request/<request_id>",
    methods=["PUT"]
)(reject_request)