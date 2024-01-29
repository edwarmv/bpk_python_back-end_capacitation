from typing import TYPE_CHECKING, List
from sqlalchemy import Boolean, Float, ForeignKey, String, SmallInteger, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

if TYPE_CHECKING:
    from app.models.hotel import Hotel
    from app.models.room_booking import RoomBooking


class Room(db.Model):
    __tablename__ = "rooms"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    room_type: Mapped[str] = mapped_column(String(30))
    price: Mapped[float] = mapped_column(Float)
    number_guests: Mapped[int] = mapped_column(SmallInteger)
    available: Mapped[bool] = mapped_column(Boolean)
    deleted: Mapped[bool] = mapped_column(Boolean)
    hotel_uui: Mapped[str] = mapped_column(ForeignKey("hotels.uuid"))

    hotel: Mapped["Hotel"] = relationship(back_populates="rooms")
    rooms_booking: Mapped[List["RoomBooking"]] = relationship(back_populates="room")
