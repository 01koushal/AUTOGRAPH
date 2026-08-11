"""Seeds CognoDB with manufacturers, cars, engines, transmissions,
drivetrains, upgrades, categories, and their relationships.

Usage:
    python seed.py            # seed (idempotent, uses MERGE)
    python seed.py --reset    # wipe the whole graph first, then seed
"""
from __future__ import annotations

import sys

from app.extensions import close_driver, get_driver
from database import apply_constraints
from seed_data import (
    CARS,
    CATEGORIES,
    DRIVETRAINS,
    ENGINES,
    MANUFACTURERS,
    SIMILAR_PAIRS,
    TRANSMISSIONS,
    UPGRADES,
)


def reset(session) -> None:
    session.run("MATCH (n) DETACH DELETE n")
    print("Cleared existing graph.")


def seed_manufacturers(session) -> None:
    session.run(
        """
        UNWIND $rows AS row
        MERGE (m:Manufacturer {slug: row.slug})
        SET m += row
        """,
        rows=MANUFACTURERS,
    )
    print(f"Seeded {len(MANUFACTURERS)} manufacturers.")


def seed_engines(session) -> None:
    session.run(
        """
        UNWIND $rows AS row
        MERGE (e:Engine {slug: row.slug})
        SET e += row
        """,
        rows=ENGINES,
    )
    print(f"Seeded {len(ENGINES)} engines.")


def seed_transmissions(session) -> None:
    session.run(
        """
        UNWIND $rows AS row
        MERGE (t:Transmission {slug: row.slug})
        SET t += row
        """,
        rows=TRANSMISSIONS,
    )
    print(f"Seeded {len(TRANSMISSIONS)} transmissions.")


def seed_drivetrains(session) -> None:
    session.run(
        """
        UNWIND $rows AS row
        MERGE (d:Drivetrain {slug: row.slug})
        SET d += row
        """,
        rows=DRIVETRAINS,
    )
    print(f"Seeded {len(DRIVETRAINS)} drivetrains.")


def seed_categories(session) -> None:
    session.run(
        """
        UNWIND $rows AS row
        MERGE (cat:Category {slug: row.slug})
        SET cat += row
        """,
        rows=CATEGORIES,
    )
    print(f"Seeded {len(CATEGORIES)} categories.")


def seed_cars(session) -> None:
    rows = [
        {
            "slug": slug,
            "name": name,
            "manufacturer": manufacturer,
            "engine": engine,
            "transmission": transmission,
            "drivetrain": drivetrain,
            "year": year,
            "horsepower": hp,
            "torque": torque,
            "bodyType": body_type,
        }
        for slug, name, manufacturer, engine, transmission, drivetrain, year, hp, torque, body_type in CARS
    ]
    session.run(
        """
        UNWIND $rows AS row
        MERGE (c:Car {slug: row.slug})
        SET c.name = row.name,
            c.year = row.year,
            c.horsepower = row.horsepower,
            c.torque = row.torque,
            c.bodyType = row.bodyType
        WITH c, row
        MATCH (m:Manufacturer {slug: row.manufacturer})
        MERGE (m)-[:MAKES]->(c)
        WITH c, row
        MATCH (e:Engine {slug: row.engine})
        MERGE (c)-[:HAS_ENGINE]->(e)
        WITH c, row
        MATCH (t:Transmission {slug: row.transmission})
        MERGE (c)-[:HAS_TRANSMISSION]->(t)
        WITH c, row
        MATCH (d:Drivetrain {slug: row.drivetrain})
        MERGE (c)-[:HAS_DRIVETRAIN]->(d)
        """,
        rows=rows,
    )
    print(f"Seeded {len(rows)} cars with MAKES / HAS_ENGINE / HAS_TRANSMISSION / HAS_DRIVETRAIN edges.")


def seed_similar(session) -> None:
    rows = [{"from": a, "to": b} for a, b in SIMILAR_PAIRS]
    session.run(
        """
        UNWIND $rows AS row
        MATCH (a:Car {slug: row.from})
        MATCH (b:Car {slug: row.to})
        MERGE (a)-[:SIMILAR_TO]->(b)
        """,
        rows=rows,
    )
    print(f"Seeded {len(rows)} SIMILAR_TO edges.")


def seed_upgrades(session) -> None:
    rows = [
        {
            "slug": slug,
            "name": name,
            "category": category,
            "description": description,
            "priceEstimate": price,
            "engines": engines,
        }
        for slug, name, category, description, price, engines in UPGRADES
    ]
    session.run(
        """
        UNWIND $rows AS row
        MERGE (u:Upgrade {slug: row.slug})
        SET u.name = row.name,
            u.description = row.description,
            u.priceEstimate = row.priceEstimate
        WITH u, row
        MATCH (cat:Category {slug: row.category})
        MERGE (u)-[:BELONGS_TO]->(cat)
        WITH u, row
        UNWIND row.engines AS engineSlug
        MATCH (e:Engine {slug: engineSlug})
        MERGE (u)-[:COMPATIBLE_WITH]->(e)
        """,
        rows=rows,
    )
    print(f"Seeded {len(rows)} upgrades with BELONGS_TO / COMPATIBLE_WITH edges.")


def main() -> None:
    do_reset = "--reset" in sys.argv
    driver = get_driver()
    with driver.session() as session:
        if do_reset:
            reset(session)
        seed_manufacturers(session)
        seed_engines(session)
        seed_transmissions(session)
        seed_drivetrains(session)
        seed_categories(session)
        seed_cars(session)
        seed_upgrades(session)
        seed_similar(session)
    apply_constraints()
    close_driver()
    print("\nSeed complete.")


if __name__ == "__main__":
    main()
