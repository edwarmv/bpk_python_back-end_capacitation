from typing import TYPE_CHECKING
from sqlalchemy import Boolean, ForeignKey, SmallInteger, Uuid, text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.extensions import db

if TYPE_CHECKING:
    from app.models.flight import Flight
    from app.models.user import User


class FlightBooking(db.Model):
    __tablename__ = "flights_booking"

    uuid: Mapped[str] = mapped_column(
        Uuid(), primary_key=True, server_default=text("uuid_generate_v4()")
    )
    number_seats: Mapped[int] = mapped_column(SmallInteger)
    canceled: Mapped[bool] = mapped_column(Boolean)
    flight_uuid: Mapped[str] = mapped_column(ForeignKey("flights.uuid"))
    user_uuid: Mapped[str] = mapped_column(ForeignKey("users.uuid"))

    flight: Mapped["Flight"] = relationship(back_populates="flights_booking")
    user: Mapped["User"] = relationship(back_populates="flights_booking")
