from __future__ import annotations

from typing import Any

from app.extensions import get_driver


class BaseRepository:
    """Thin helper around the Neo4j driver for running Cypher queries."""

    def read(self, query: str, **params: Any) -> list[dict]:
        driver = get_driver()
        with driver.session() as session:
            result = session.run(query, **params)
            return [record.data() for record in result]

    def write(self, query: str, **params: Any) -> list[dict]:
        driver = get_driver()
        with driver.session() as session:
            result = session.execute_write(lambda tx: list(tx.run(query, **params)))
            return [record.data() for record in result]
