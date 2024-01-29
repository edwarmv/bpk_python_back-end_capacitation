from datetime import datetime
from typing import TYPE_CHECKING, List
from sqlalchemy import Boolean, DateTime, Float, String, SmallInteger, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

if TYPE_CHECKING:
    from app.models.flight_booking import FlightBooking


class Flight(db.Model):
    __tablename__ = "flights"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    airlane_name: Mapped[str] = mapped_column(String(20))
    from_location: Mapped[str] = mapped_column(String(60))
    to_location: Mapped[str] = mapped_column(String(60))
    departure_time: Mapped[datetime] = mapped_column(DateTime)
    arrival_time: Mapped[datetime] = mapped_column(DateTime)
    total_seats: Mapped[int] = mapped_column(SmallInteger)
    price: Mapped[float] = mapped_column(Float)
    canceled: Mapped[bool] = mapped_column(Boolean)

    flights_booking: Mapped[List["FlightBooking"]] = relationship(
        back_populates="flight"
    )
