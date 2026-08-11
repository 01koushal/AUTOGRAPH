from __future__ import annotations

from app.repositories.car_repository import CarRepository


class CarService:
    def __init__(self, repo: CarRepository | None = None) -> None:
        self.repo = repo or CarRepository()

    def list_cars(self):
        return self.repo.list_cars()

    def recent_cars(self):
        return self.repo.recent_cars()

    def get_car(self, slug: str):
        detail = self.repo.get_car_detail(slug)
        if detail is None:
            return None
        detail["engineFamilyCars"] = self.repo.cars_sharing_engine_family(slug)
        detail["recommended"] = self.repo.recommend_by_shared_traits(slug)
        return detail

    def search(self, term: str):
        term = (term or "").strip()
        if not term:
            return []
        return self.repo.search(term)
