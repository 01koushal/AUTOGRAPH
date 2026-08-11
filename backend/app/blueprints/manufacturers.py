from __future__ import annotations

from flask import Blueprint, abort, jsonify

from app.services.manufacturer_service import ManufacturerService

manufacturers_bp = Blueprint("manufacturers", __name__)
service = ManufacturerService()


@manufacturers_bp.get("")
def list_manufacturers():
    return jsonify(service.list_manufacturers())


@manufacturers_bp.get("/popular")
def popular_manufacturers():
    return jsonify(service.popular())


@manufacturers_bp.get("/<slug>")
def get_manufacturer(slug: str):
    manufacturer = service.get_manufacturer(slug)
    if manufacturer is None:
        abort(404, description=f"Manufacturer '{slug}' not found")
    return jsonify(manufacturer)
