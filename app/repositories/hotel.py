from sqlalchemy import select
from flask_restful import marshal_with, fields

from app.extensions import db
from app.models import Hotel

hotel_fields = {
    "uuid": fields.String,
    "name": fields.String,
    "country": fields.String,
    "city": fields.String,
    "address": fields.String,
}


class HotelRepository:
    db = db.session
    model = Hotel

    def add(self, entity: Hotel):
        self.db.add(entity)
        self.db.commit()

    @marshal_with(hotel_fields)
    def get_all(self):
        query = select(self.model)
        hotels = self.db.execute(query).scalars().all()
        return hotels

    @marshal_with(hotel_fields)
    def get_by_uuid(self, uuid: str):
        query = select(self.model).where(self.model.uuid == uuid)
        hotel = self.db.execute(query).scalar_one()
        return hotel
