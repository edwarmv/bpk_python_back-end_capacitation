from typing import Optional

from sqlalchemy import select

from app.models import Room
from app.extensions import db


class RoomRepository:
    model = Room
    db = db.session

    def add(self, entity: Room) -> None:
        self.db.add(entity)
        self.db.commit()

    def update(
        self,
        uuid: str,
        room_type: Optional[str] = None,
        price: Optional[float] = None,
        number_guests: Optional[int] = None,
        available: Optional[bool] = None,
        hotel_uuid: Optional[str] = None,
    ):
        query = select(self.model).where(self.model.uuid == uuid)
        room = self.db.execute(query).scalar_one()

        if room_type:
            room.room_type = room_type

        if price:
            room.price = price

        if number_guests:
            room.number_guests = number_guests

        if available:
            room.available = available

        if hotel_uuid:
            room.hotel_uuid = hotel_uuid

        self.db.commit()

    def delete(self, uuid: str):
        query = select(self.model).where(self.model.uuid == uuid)
        room = self.db.execute(query).scalar_one()

        room.deleted = True

        self.db.commit()

    def get_all(self):
        query = select(self.model)
        rooms = self.db.execute(query).scalars().all()
        return rooms

    def get_by_uuid(self, uuid: str) -> Room:
        query = select(self.model).where(self.model.uuid == uuid)
        room = self.db.execute(query).scalar_one()

        return room
