from typing import Optional
from sqlalchemy import select

from app.extensions import db
from app.models import Hotel


class HotelRepository:
    db = db.session
    model = Hotel

    def add(self, entity: Hotel):
        self.db.add(entity)
        self.db.commit()

    def update(
        self,
        uuid: str,
        name: Optional[str] = None,
        country: Optional[str] = None,
        city: Optional[str] = None,
        address: Optional[str] = None,
    ):
        query = select(self.model).where(self.model.uuid == uuid)
        hotel = self.db.execute(query).scalar_one()

        if name:
            hotel.name = name
        if country:
            hotel.country = country
        if city:
            hotel.city = city
        if address:
            hotel.address = address

        self.db.commit()

    def get_all(self):
        query = select(self.model)
        hotels = self.db.execute(query).scalars().all()
        return hotels

    def get_by_uuid(self, uuid: str):
        query = select(self.model).where(self.model.uuid == uuid)
        hotel = self.db.execute(query).scalar_one()
        return hotel
