from typing import List

from flask_restful import fields, marshal_with
from sqlalchemy import select

from app.models import User
from app.extensions import db

user_fields = {
    "uuid": fields.String,
    "full_name": fields.String,
    "role": fields.String,
    "deleted": fields.Boolean,
}


class UserRepository:
    model = User
    db = db.session

    @marshal_with(user_fields)
    def get_all(self) -> List[User]:
        users = self.db.query(self.model).all()
        return users

    @marshal_with(user_fields)
    def get_by_uuid(self, uuid: str) -> User:
        query = select(self.model).where(self.model.uuid == uuid)
        user = self.db.execute(query).scalar_one()
        return user

    def add(self, entity: User) -> None:
        self.db.add(entity)
        self.db.commit()

    def update(self, entity: User) -> None:
        pass
        # self.db.