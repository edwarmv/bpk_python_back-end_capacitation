from flask_restful import Resource, fields, marshal, marshal_with, reqparse, inputs

from app.helpers import is_valid_uuid
from app.models import RoomBooking
from app.repositories import RoomBookingRepository

user_fields = {"uuid": fields.String, "full_name": fields.String}

hotel_fields = {
    "uuid": fields.String,
    "name": fields.String,
}

room_fields = {
    "uuid": fields.String,
    "room_type": fields.String,
    "price": fields.Float,
    "number_guests": fields.Integer,
    "hotel": fields.Nested(hotel_fields),
}

room_booking_fields = {
    "uuid": fields.String,
    "from_date": fields.String,
    "to_date": fields.String,
    "canceled": fields.Boolean,
    "user": fields.Nested(user_fields),
    "room": fields.Nested(room_fields),
}


class RoomBookingResource(Resource):
    repository = RoomBookingRepository()

    def get(self, uuid: str):
        if not is_valid_uuid(uuid):
            return "the passed uuid is not a valid uuid", 400

        room_booking = self.repository.get_by_uuid(uuid)

        return marshal(room_booking, room_booking_fields)

    def patch(self, uuid: str):
        if not is_valid_uuid(uuid):
            return "the passed uuid is not a valid uuid", 400

        parser = reqparse.RequestParser()
        parser.add_argument("from_date", type=inputs.date)
        parser.add_argument("to_date", type=inputs.date)
        parser.add_argument("canceled", type=bool)
        parser.add_argument("user_uuid", type=str)
        parser.add_argument("room_uuid", type=str)

        args = parser.parse_args()

        self.repository.update(
            uuid,
            from_date=args["from_date"],
            to_date=args["to_date"],
            canceled=args["canceled"],
            user_uuid=args["user_uuid"],
            room_uuid=args["room_uuid"],
        )

        return "room booking was successfully updated"


class RoomsBookingResource(Resource):
    repository = RoomBookingRepository()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("from_date", type=inputs.date, required=True)
        parser.add_argument("to_date", type=inputs.date, required=True)
        parser.add_argument("user_uuid", type=str, required=True)
        parser.add_argument("room_uuid", type=str, required=True)

        args = parser.parse_args()

        room_booking = RoomBooking(
            from_date=args["from_date"],
            to_date=args["to_date"],
            user_uuid=args["user_uuid"],
            room_uuid=args["room_uuid"],
        )

        self.repository.add(room_booking)

        return "room booking was created successfully", 201

    @marshal_with(room_booking_fields)
    def get(self):
        rooms_booking = self.repository.get_all()

        return rooms_booking
