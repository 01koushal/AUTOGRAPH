from __future__ import annotations

from app.repositories.manufacturer_repository import ManufacturerRepository


class ManufacturerService:
    def __init__(self, repo: ManufacturerRepository | None = None) -> None:
        self.repo = repo or ManufacturerRepository()

    def list_manufacturers(self):
        return self.repo.list_manufacturers()

    def popular(self):
        return self.repo.popular_manufacturers()

    def get_manufacturer(self, slug: str):
        detail = self.repo.get_manufacturer_detail(slug)
        if detail is None:
            return None
        detail["relatedManufacturers"] = self.repo.shared_engine_manufacturers(slug)
        return detail
