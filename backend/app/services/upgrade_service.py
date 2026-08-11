from __future__ import annotations

from app.repositories.upgrade_repository import UpgradeRepository


class UpgradeService:
    def __init__(self, repo: UpgradeRepository | None = None) -> None:
        self.repo = repo or UpgradeRepository()

    def list_upgrades(self, category: str | None = None):
        return self.repo.list_upgrades(category)

    def list_categories(self):
        return self.repo.list_categories()
