from __future__ import annotations

import logging

from flask import Flask, jsonify
from flask_cors import CORS
from neo4j.exceptions import Neo4jError, ServiceUnavailable

from app.config import config
from app.extensions import close_driver, verify_connectivity


def create_app() -> Flask:
    app = Flask(__name__)
    logging.basicConfig(level=logging.INFO)

    CORS(app, resources={r"/api/*": {"origins": config.cors_origin_list}})

    from app.blueprints.cars import cars_bp
    from app.blueprints.manufacturers import manufacturers_bp
    from app.blueprints.upgrades import upgrades_bp
    from app.blueprints.search import search_bp
    from app.blueprints.meta import meta_bp

    app.register_blueprint(meta_bp, url_prefix="/api")
    app.register_blueprint(cars_bp, url_prefix="/api/cars")
    app.register_blueprint(manufacturers_bp, url_prefix="/api/manufacturers")
    app.register_blueprint(upgrades_bp, url_prefix="/api/upgrades")
    app.register_blueprint(search_bp, url_prefix="/api/search")

    @app.errorhandler(ServiceUnavailable)
    def handle_service_unavailable(exc):
        app.logger.error("CognoDB unavailable: %s", exc)
        return jsonify(error="Graph database is unreachable. Please try again shortly."), 503

    @app.errorhandler(Neo4jError)
    def handle_neo4j_error(exc):
        app.logger.error("CognoDB query error: %s", exc)
        return jsonify(error="A graph database error occurred.", detail=str(exc)), 500

    @app.errorhandler(404)
    def handle_not_found(exc):
        return jsonify(error="Resource not found."), 404

    @app.errorhandler(Exception)
    def handle_unexpected(exc):
        app.logger.exception("Unexpected error")
        return jsonify(error="Internal server error."), 500

    @app.teardown_appcontext
    def _teardown(exception=None):  # noqa: ARG001
        pass

    app.config["JSON_SORT_KEYS"] = False

    return app


__all__ = ["create_app", "close_driver", "verify_connectivity"]
