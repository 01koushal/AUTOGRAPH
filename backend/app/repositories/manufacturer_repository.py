from __future__ import annotations

from app.repositories.base import BaseRepository


class ManufacturerRepository(BaseRepository):
    def list_manufacturers(self) -> list[dict]:
        query = """
        MATCH (m:Manufacturer)
        OPTIONAL MATCH (m)-[:MAKES]->(c:Car)
        RETURN m { .*, carCount: count(DISTINCT c) } AS manufacturer
        ORDER BY m.name
        """
        rows = self.read(query)
        return [r["manufacturer"] for r in rows]

    def popular_manufacturers(self, limit: int = 6):
        query = """
        MATCH (m:Manufacturer)-[:MAKES]->(c:Car)
        RETURN m.name AS name,
            m.slug AS slug,
            count(c) AS carCount
        ORDER BY carCount DESC
        LIMIT $limit
        """
        return self.read(query, limit=limit)

    def get_manufacturer_detail(self, slug: str) -> dict | None:
        query = """
        MATCH (m:Manufacturer {slug: $slug})
        OPTIONAL MATCH (m)-[:MAKES]->(c:Car)
        OPTIONAL MATCH (c)-[:HAS_ENGINE]->(e:Engine)
        RETURN m { .* } AS manufacturer,
               collect(DISTINCT c { .name, .slug, .year, .horsepower }) AS cars,
               collect(DISTINCT e { .name, .slug, .family }) AS engines
        """
        rows = self.read(query, slug=slug)
        return rows[0] if rows else None

    def shared_engine_manufacturers(self, slug: str, limit: int = 8) -> list[dict]:
        """2-hop traversal: Manufacturer -> Car -> Engine <- Car <- Manufacturer."""
        query = """
        MATCH (m:Manufacturer {slug: $slug})-[:MAKES]->(:Car)-[:HAS_ENGINE]->(e:Engine)
        MATCH (otherM:Manufacturer)-[:MAKES]->(:Car)-[:HAS_ENGINE]->(e)
        WHERE otherM.slug <> $slug
        RETURN DISTINCT otherM { .name, .slug } AS manufacturer, collect(DISTINCT e.family) AS sharedEngineFamilies
        LIMIT $limit
        """
        rows = self.read(query, slug=slug, limit=limit)
        return rows
