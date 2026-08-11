"""Shared, process-wide extensions: the Neo4j/CognoDB driver.

CognoDB speaks the Bolt protocol and is fully compatible with the
official `neo4j` Python driver, so no CognoDB-specific client is needed.
"""
from __future__ import annotations

import logging

from neo4j import Driver, GraphDatabase

from app.config import config

logger = logging.getLogger(__name__)

_driver: Driver | None = None


def get_driver() -> Driver:
    """Return a lazily-created, process-wide Neo4j/CognoDB driver."""
    global _driver
    if _driver is None:
        _driver = GraphDatabase.driver(
            config.graph_uri,
            auth=(config.graph_user, config.graph_password),
        )
    return _driver


def verify_connectivity() -> bool:
    try:
        get_driver().verify_connectivity()
        return True
    except Exception as exc:  # noqa: BLE001
        logger.error("CognoDB connectivity check failed: %s", exc)
        return False


def close_driver() -> None:
    global _driver
    if _driver is not None:
        _driver.close()
        _driver = None
