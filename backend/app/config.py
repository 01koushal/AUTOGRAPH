"""Application configuration loaded from environment variables.

Only three values ever need to change to run this project against a
different CognoDB / Neo4j instance: GRAPH_URI, GRAPH_USER, GRAPH_PASSWORD.
"""
import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    graph_uri: str = os.environ.get("GRAPH_URI", "bolt://localhost:7687")
    graph_user: str = os.environ.get("GRAPH_USER", "neo4j")
    graph_password: str = os.environ.get("GRAPH_PASSWORD", "neo4j")
    port: int = int(os.environ.get("PORT", 5000))
    cors_origins: str = os.environ.get("CORS_ORIGINS", "*")
    flask_env: str = os.environ.get("FLASK_ENV", "development")

    @property
    def cors_origin_list(self) -> list[str]:
        if self.cors_origins.strip() == "*":
            return ["*"]
        return [o.strip() for o in self.cors_origins.split(",") if o.strip()]


config = Config()
