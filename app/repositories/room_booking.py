from datetime import date
from typing import Optional
from sqlalchemy import select

from app.models import RoomBooking, room
from app.extensions import db


class RoomBookingRepository:
    model = RoomBooking
    db = db.session

    def add(self, entity: RoomBooking) -> None:
        self.db.add(entity)
        self.db.commit()

    def get_all(self):
        query = select(self.model)

        rooms_booking = self.db.execute(query).scalars().all()

        return rooms_booking

    def get_by_uuid(self, uuid: str):
        query = select(self.model).where(self.model.uuid == uuid)

        room_booking = self.db.execute(query).scalar_one()

        return room_booking

    def update(
        self,
        uuid: str,
        from_date: Optional[date] = None,
        to_date: Optional[date] = None,
        canceled: Optional[bool] = None,
        user_uuid: Optional[str] = None,
        room_uuid: Optional[str] = None,
    ):
        room_booking = self.get_by_uuid(uuid)

        if from_date:
            room_booking.from_date = from_date
        if to_date:
            room_booking.to_date = to_date
        if canceled:
            room_booking.canceled = canceled
        if user_uuid:
            room_booking.user_uuid = user_uuid
        if room_uuid:
            room_booking.room_uuid = room_uuid

        self.db.commit()
