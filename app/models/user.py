from typing import TYPE_CHECKING, List
from sqlalchemy import Boolean, String, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

if TYPE_CHECKING:
    from app.models.flight_booking import FlightBooking
    from app.models.room_booking import RoomBooking


class User(db.Model):
    __tablename__ = "users"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    full_name: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(60))
    role: Mapped[str] = mapped_column(String(20))
    deleted: Mapped[bool] = mapped_column(Boolean)

    flights_booking: Mapped[List["FlightBooking"]] = relationship(back_populates="user")
    rooms_booking: Mapped[List["RoomBooking"]] = relationship(back_populates="user")
