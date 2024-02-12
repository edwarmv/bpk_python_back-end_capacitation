from datetime import date
from typing import TYPE_CHECKING
from sqlalchemy import Boolean, Date, ForeignKey, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

if TYPE_CHECKING:
    from app.models.room import Room
    from app.models.user import User


class RoomBooking(db.Model):
    __tablename__ = "rooms_booking"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    from_date: Mapped[date] = mapped_column(Date)
    to_date: Mapped[date] = mapped_column(Date)
    canceled: Mapped[bool] = mapped_column(Boolean)
    user_uuid: Mapped[str] = mapped_column(ForeignKey("users.uuid"))
    room_uuid: Mapped[str] = mapped_column(ForeignKey("rooms.uuid"))

    user: Mapped["User"] = relationship(back_populates="rooms_booking")
    room: Mapped["Room"] = relationship(back_populates="rooms_booking")
