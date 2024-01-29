from typing import TYPE_CHECKING, List
from sqlalchemy import String, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

if TYPE_CHECKING:
    from app.models.room import Room


class Hotel(db.Model):
    __tablename__ = "hotels"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    name: Mapped[str] = mapped_column(String(50))
    country: Mapped[str] = mapped_column(String(30))
    city: Mapped[str] = mapped_column(String(40))
    address: Mapped[str] = mapped_column(String(60))

    rooms: Mapped[List["Room"]] = relationship(back_populates="hotel")
