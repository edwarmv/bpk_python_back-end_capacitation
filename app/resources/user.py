from flask_restful import Resource, reqparse

from app.repositories import UserRepository
from app.models import User
from app.helpers import is_valid_uuid


class UserResource(Resource):
    userRepository = UserRepository()

    def get(self, uuid: str):
        if uuid:
            if not is_valid_uuid(uuid):
                return "the passed uuid is not a valid uuid", 400

            try:
                user = self.userRepository.get_by_uuid(uuid)
                return user
            except:
                return f"there is no an user with uuid: {uuid}", 404

        return self.userRepository.get_all()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument("full_name", type=str, required=True)
        parser.add_argument("password", type=str, required=True)
        parser.add_argument("role", choices=["admin", "user"], required=True)
        args = parser.parse_args()
        user = User(
            full_name=args["full_name"], password=args["password"], role=args["role"]
        )
        self.userRepository.add(user)
        return "user created successfully", 201

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument("/")