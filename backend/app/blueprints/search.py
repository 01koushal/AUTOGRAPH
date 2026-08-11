from __future__ import annotations

from flask import Blueprint, jsonify, request

from app.services.car_service import CarService

search_bp = Blueprint("search", __name__)
service = CarService()


@search_bp.get("")
def search():
    term = request.args.get("q", "")
    return jsonify(service.search(term))
