from __future__ import annotations

from flask import Blueprint, jsonify, request

from app.services.upgrade_service import UpgradeService

upgrades_bp = Blueprint("upgrades", __name__)
service = UpgradeService()


@upgrades_bp.get("")
def list_upgrades():
    category = request.args.get("category")
    return jsonify(service.list_upgrades(category))


@upgrades_bp.get("/categories")
def list_categories():
    return jsonify(service.list_categories())
