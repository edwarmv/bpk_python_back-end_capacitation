from flask_restful import Resource, reqparse

from app.repositories import HotelRepository
from app.models import Hotel
from app.helpers import is_valid_uuid


class HotelResource(Resource):
    hotelRepository = HotelRepository()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("name", type=str, required=True)
        parser.add_argument("country", type=str, required=True)
        parser.add_argument("city", type=str, required=True)
        parser.add_argument("address", type=str, required=True)
        args = parser.parse_args()

        hotel = Hotel(
            name=args["name"],
            country=args["country"],
            city=args["city"],
            address=args["address"],
        )

        self.hotelRepository.add(hotel)

        return "hotel created successfully", 200

    def get(self, uuid: str):
        if not is_valid_uuid(uuid):
            return "the passed uuid is not a valid uuid", 400

        try:
            hotel = self.hotelRepository.get_by_uuid(uuid)
            return hotel
        except:
            return f"there is no an hotel with uuid: {uuid}", 404


class HotelsResource(Resource):
    hotelRepository = HotelRepository()

    def get(self):
        return self.hotelRepository.get_all()
