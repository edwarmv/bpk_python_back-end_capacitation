from flask_restful import Resource, fields, marshal_with, reqparse
from app.helpers import is_valid_uuid

from app.models import Room
from app.repositories import RoomRepository

room_fields = {
    "uuid": fields.String,
    "price": fields.Float,
    "number_guests": fields.Integer,
    "available": fields.Boolean,
    "deleted": fields.Boolean,
}


class RoomResource(Resource):
    roomRepository = RoomRepository()

    @marshal_with(room_fields)
    def get(self, uuid: str):
        if not is_valid_uuid(uuid):
            return "the passed uuid is not a valid uuid", 400

        room = self.roomRepository.get_by_uuid(uuid)

        return room

    def patch(self, uuid: str):
        if not is_valid_uuid(uuid):
            return "the passed uuid is not a valid uuid", 400

        parser = reqparse.RequestParser()
        parser.add_argument("room_type", type=str)
        parser.add_argument("price", type=float)
        parser.add_argument("number_guests", type=int)
        parser.add_argument("available", type=bool)
        parser.add_argument("hotel_uuid", type=str)

        args = parser.parse_args()

        self.roomRepository.update(
            uuid,
            room_type=args["room_type"],
            price=args["price"],
            number_guests=args["number_guests"],
            available=args["available"],
            hotel_uuid=args["hotel_uuid"],
        )

        return "room was updated successfully"

    def delete(self, uuid: str):
        self.roomRepository.delete(uuid)

        return "room was deleted successfully"


class RoomsResource(Resource):
    roomRepository = RoomRepository()

    @marshal_with(room_fields)
    def get(self):
        return self.roomRepository.get_all()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("room_type", type=str, required=True)
        parser.add_argument("price", type=float, required=True)
        parser.add_argument("number_guests", type=int, required=True)
        parser.add_argument("available", type=bool, required=True)
        parser.add_argument("hotel_uuid", type=str, required=True)

        args = parser.parse_args()

        room = Room(
            room_type=args["room_type"],
            price=args["price"],
            number_guests=args["number_guests"],
            available=args["available"],
            hotel_uuid=args["hotel_uuid"],
        )

        self.roomRepository.add(room)

        return "room was created successfully", 201
