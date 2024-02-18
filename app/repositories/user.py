from typing import List, Literal, Optional

from sqlalchemy import select

from app.models import User
from app.extensions import db


class UserRepository:
    model = User
    db = db.session

    def get_all(self) -> List[User]:
        users = self.db.query(self.model).all()
        return users

    def get_by_uuid(self, uuid: str) -> User:
        query = select(self.model).where(self.model.uuid == uuid)
        user = self.db.execute(query).scalar_one()
        return user

    def add(self, entity: User) -> None:
        self.db.add(entity)
        self.db.commit()

    def update(
        self,
        uuid: str,
        full_name: Optional[str] = None,
        password: Optional[str] = None,
        role: Optional[Literal["admin", "user"]] = None,
    ) -> None:
        query = select(self.model).where(self.model.uuid == uuid)
        user = self.db.execute(query).scalar_one()
        if full_name:
            user.full_name = full_name
        if password:
            user.password = password
        if role:
            user.role = role
        self.db.commit()

    def delete(self, uuid: str):
        query = select(self.model).where(self.model.uuid == uuid)
        user = self.db.execute(query).scalar_one()
        user.deleted = True
        self.db.commit()
