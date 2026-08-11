from __future__ import annotations

from flask import Blueprint, jsonify

from app.extensions import verify_connectivity

meta_bp = Blueprint("meta", __name__)


@meta_bp.get("/health")
def health():
    connected = verify_connectivity()
    status = "ok" if connected else "degraded"
    return jsonify(status=status, graphConnected=connected), 200 if connected else 503
