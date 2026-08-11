from __future__ import annotations

from app.repositories.base import BaseRepository


class CarRepository(BaseRepository):
    def list_cars(self, limit: int = 100) -> list[dict]:
        query = """
        MATCH (m:Manufacturer)-[:MAKES]->(c:Car)
        OPTIONAL MATCH (c)-[:HAS_ENGINE]->(e:Engine)
        RETURN c { .*, manufacturer: m.name, manufacturerSlug: m.slug,
                    engine: e.name } AS car
        ORDER BY c.name
        LIMIT $limit
        """
        rows = self.read(query, limit=limit)
        return [r["car"] for r in rows]

    def recent_cars(self, limit: int = 6) -> list[dict]:
        query = """
        MATCH (m:Manufacturer)-[:MAKES]->(c:Car)
        RETURN c { .*, manufacturer: m.name, manufacturerSlug: m.slug } AS car
        ORDER BY c.year DESC
        LIMIT $limit
        """
        rows = self.read(query, limit=limit)
        return [r["car"] for r in rows]

    def get_car_detail(self, slug: str) -> dict | None:
        """Single traversal pulling every direct relationship of a car,
        plus a 2-hop reach into shared-engine 'family' cars."""
        query = """
        MATCH (m:Manufacturer)-[:MAKES]->(c:Car {slug: $slug})
        OPTIONAL MATCH (c)-[:HAS_ENGINE]->(e:Engine)
        OPTIONAL MATCH (c)-[:HAS_TRANSMISSION]->(t:Transmission)
        OPTIONAL MATCH (c)-[:HAS_DRIVETRAIN]->(d:Drivetrain)
        OPTIONAL MATCH (c)-[:SIMILAR_TO]->(sim:Car)<-[:MAKES]-(simM:Manufacturer)
        OPTIONAL MATCH (up:Upgrade)-[:COMPATIBLE_WITH]->(e)
        OPTIONAL MATCH (up)-[:BELONGS_TO]->(cat:Category)
        RETURN c { .* } AS car,
               m { .name, .slug } AS manufacturer,
               e { .* } AS engine,
               t { .* } AS transmission,
               d { .* } AS drivetrain,
               collect(DISTINCT sim { .name, .slug, .year, manufacturer: simM.name }) AS similarCars,
               collect(DISTINCT up { .name, .slug, .description, .priceEstimate, category: cat.name }) AS upgrades
        """
        rows = self.read(query, slug=slug)
        if not rows:
            return None
        return rows[0]

    def cars_sharing_engine_family(self, slug: str, limit: int = 8) -> list[dict]:
        """2-hop traversal: Car -> Engine (by family) <- Car, excluding self."""
        query = """
        MATCH (c:Car {slug: $slug})-[:HAS_ENGINE]->(e:Engine)
        MATCH (other:Car)-[:HAS_ENGINE]->(e2:Engine)
        WHERE other.slug <> $slug AND e2.family = e.family
        MATCH (om:Manufacturer)-[:MAKES]->(other)
        RETURN DISTINCT other { .name, .slug, .year, .horsepower,
                                 manufacturer: om.name, engineFamily: e2.family } AS car
        LIMIT $limit
        """
        rows = self.read(query, slug=slug, limit=limit)
        return [r["car"] for r in rows]

    def recommend_by_shared_traits(self, slug: str, limit: int = 6) -> list[dict]:
        """Multi-hop recommendation: cars sharing BOTH drivetrain and engine
        family are ranked above cars sharing only one trait."""
        query = """
        MATCH (c:Car {slug: $slug})-[:HAS_DRIVETRAIN]->(d:Drivetrain)
        MATCH (c)-[:HAS_ENGINE]->(e:Engine)
        MATCH (other:Car)-[:HAS_DRIVETRAIN]->(d)
        MATCH (other)-[:HAS_ENGINE]->(e2:Engine)
        WHERE other.slug <> $slug
        WITH other, d, e, e2,
             (CASE WHEN e2.family = e.family THEN 1 ELSE 0 END) AS engineMatch
        MATCH (om:Manufacturer)-[:MAKES]->(other)
        RETURN other { .name, .slug, .year, .horsepower,
                        manufacturer: om.name, drivetrain: d.name,
                        sharedEngineFamily: engineMatch = 1 } AS car,
               engineMatch
        ORDER BY engineMatch DESC, other.horsepower DESC
        LIMIT $limit
        """
        rows = self.read(query, slug=slug, limit=limit)
        return [r["car"] for r in rows]

    def search(self, term: str, limit: int = 12) -> list[dict]:
        query = """
        MATCH (m:Manufacturer)-[:MAKES]->(c:Car)
        WHERE toLower(c.name) CONTAINS toLower($term)
           OR toLower(m.name) CONTAINS toLower($term)
        RETURN c { .*, manufacturer: m.name, manufacturerSlug: m.slug } AS car
        LIMIT $limit
        """
        rows = self.read(query, term=term, limit=limit)
        return [r["car"] for r in rows]
