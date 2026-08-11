from __future__ import annotations

from app.repositories.base import BaseRepository


class UpgradeRepository(BaseRepository):
    def list_upgrades(self, category: str | None = None) -> list[dict]:
        query = """
        MATCH (u:Upgrade)-[:BELONGS_TO]->(cat:Category)
        WHERE $category IS NULL OR toLower(cat.slug) = toLower($category)
        OPTIONAL MATCH (u)-[:COMPATIBLE_WITH]->(e:Engine)
        RETURN u { .*, category: cat.name, categorySlug: cat.slug,
                    compatibleEngines: collect(DISTINCT e.name) } AS upgrade
        ORDER BY u.name
        """
        rows = self.read(query, category=category)
        return [r["upgrade"] for r in rows]

    def list_categories(self) -> list[dict]:
        query = """
        MATCH (cat:Category)
        OPTIONAL MATCH (u:Upgrade)-[:BELONGS_TO]->(cat)
        RETURN cat { .*, upgradeCount: count(u) } AS category
        ORDER BY cat.name
        """
        rows = self.read(query)
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
