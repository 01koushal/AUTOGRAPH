from __future__ import annotations

import logging

from app.repositories.base import BaseRepository

logger = logging.getLogger(__name__)


class UpgradeRepository(BaseRepository):
    def list_upgrades(self, category: str | None = None) -> list[dict]:
        query = """
        MATCH (u:Upgrade)-[:BELONGS_TO]->(cat:Category)
        WHERE $category IS NULL OR toLower(cat.slug) = toLower($category)
        OPTIONAL MATCH (u)-[:COMPATIBLE_WITH]->(e:Engine)
        WITH u, cat, collect(DISTINCT e.name) AS compatibleEngines
        RETURN u { .*, category: cat.name, categorySlug: cat.slug,
                    compatibleEngines: compatibleEngines } AS upgrade
        ORDER BY u.name
        """
        rows = self.read(query, category=category)
        return [r["upgrade"] for r in rows]

    def list_categories(self) -> list[dict]:
        query = """
        MATCH (cat:Category)
        OPTIONAL MATCH (u:Upgrade)-[:BELONGS_TO]->(cat)
        WITH cat, count(u) AS upgradeCount
        RETURN cat { .*, upgradeCount: upgradeCount } AS category
        ORDER BY cat.name
        """
        rows = self.read(query)
        logger.debug("Raw upgrade category rows: %s", rows)
        return [r["category"] for r in rows]

    def compatible_upgrades_for_engine_slug(self, engine_slug: str) -> list[dict]:
        query = """
        MATCH (u:Upgrade)-[:COMPATIBLE_WITH]->(e:Engine {slug: $engine_slug})
        OPTIONAL MATCH (u)-[:BELONGS_TO]->(cat:Category)
        RETURN u { .*, category: cat.name } AS upgrade
        ORDER BY u.name
        """
        rows = self.read(query, engine_slug=engine_slug)
        return [r["upgrade"] for r in rows]
