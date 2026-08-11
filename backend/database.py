"""Standalone connectivity + schema utility for CognoDB.

Run directly to verify the driver can reach the database and to create
uniqueness constraints (which also speed up MATCH-by-slug lookups).

    python database.py
"""
from __future__ import annotations

from app.config import config
from app.extensions import close_driver, get_driver

CONSTRAINTS = [
    "CREATE CONSTRAINT manufacturer_slug IF NOT EXISTS FOR (m:Manufacturer) REQUIRE m.slug IS UNIQUE",
    "CREATE CONSTRAINT car_slug IF NOT EXISTS FOR (c:Car) REQUIRE c.slug IS UNIQUE",
    "CREATE CONSTRAINT engine_slug IF NOT EXISTS FOR (e:Engine) REQUIRE e.slug IS UNIQUE",
    "CREATE CONSTRAINT transmission_slug IF NOT EXISTS FOR (t:Transmission) REQUIRE t.slug IS UNIQUE",
    "CREATE CONSTRAINT drivetrain_slug IF NOT EXISTS FOR (d:Drivetrain) REQUIRE d.slug IS UNIQUE",
    "CREATE CONSTRAINT upgrade_slug IF NOT EXISTS FOR (u:Upgrade) REQUIRE u.slug IS UNIQUE",
    "CREATE CONSTRAINT category_slug IF NOT EXISTS FOR (cat:Category) REQUIRE cat.slug IS UNIQUE",
]


def apply_constraints() -> None:
    driver = get_driver()
    with driver.session() as session:
        for stmt in CONSTRAINTS:
            session.run(stmt)
    print(f"Applied {len(CONSTRAINTS)} uniqueness constraints.")


def main() -> None:
    print(f"Connecting to {config.graph_uri} ...")
    driver = get_driver()
    driver.verify_connectivity()
    print("Connection OK.")
    apply_constraints()
    close_driver()


if __name__ == "__main__":
    main()
