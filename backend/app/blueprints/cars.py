from __future__ import annotations

from flask import Blueprint, abort, jsonify

from app.services.car_service import CarService

cars_bp = Blueprint("cars", __name__)
service = CarService()


@cars_bp.get("")
def list_cars():
    return jsonify(service.list_cars())


@cars_bp.get("/recent")
def recent_cars():
    return jsonify(service.recent_cars())


@cars_bp.get("/<slug>")
def get_car(slug: str):
    car = service.get_car(slug)
    if car is None:
        abort(404, description=f"Car '{slug}' not found")
    return jsonify(car)
